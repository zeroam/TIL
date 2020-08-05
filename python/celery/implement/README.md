## Celery

### 참조링크

- [Understand how celery works by building a clone](https://www.komu.engineer/blogs/celery-clone/understand-how-celery-works)



### Intro

- delayed job processor(또는 background process, asynchronous task queue 등으로 불림)는 나중에 코드를 실행할 수 있는 소프트웨어 시스템이다.

- 이러한 소프트웨어의 예로는 [Celery](https://github.com/celery/celery), [Resque](https://github.com/resque/resque), [Sidekiq](https://sidekiq.org/) 등이 있다

- background task processor가 필요한 경우
  - 전자상거래(e-commerce) 웹사이트>
  - 주문 확인 메시지 표시
  - 데이터베이스에 대한 주문 승인
  - 주문 메트릭 이벤트 전송
  - 고객에게 확인 이메일 보내기
  - 등등
  



### How they work

작업 프로세서는 다를 수 있으나, 대부분 다음과 같이 동작함
1. IO 작업 또는 그 외의 작업들로 인해 실행시간이 긴 함수가 있다.
2. '백그라운드 작업' 라이브러리에서 제공하는 일부 기능을 사용하여 해당 함수를 백그라운드 작업에 추가(annotation)할 수 있다.
3. 함수를 실행(execute)할 때 코드 상에서 동시에(synchronously) 실행하는 대신에 '백그라운드 작업' 라이브러리가 해당 함수를 받아(take) 객체로 serialize 한다(ex. string)
4. '백그라운드 작업' 라이브러리가 serialized 된 객체를 받아 어딘가에 저장한다(ex. 데이터베이스)
5. 나중에, workers(백그라운드 작업 라이브러리에 의해 제공되는) serialized 된 객체를 저장소로부터 받아와 원래의 형태로 변환한다(convert/deserialize)
6. 그것을 원래 함수를 실행하기 위해 사용한다



### Implementation

예제에서는 백그라운드 작업 라이브러리 backie 를 구현할 것이다

#### (a) Base-Task

- 모든 backie 사용자가 하위 클래스를 만들어야 할 기본 작업(base-task) 클래스
- 백그라운드에서 처리될 작업(task)를 생성하려면 backie에서 BaseTask를 가져와 하위 클래스를 생성하고 run 메서드를 구현해야 함. 
- delay 메서드를 적절한 인수와 함께 호출하면 BaseTask는 이러한 인수들과 작업 id를 json 데이터로 전환(serialize)해서 BaseTask.broker에 저장함

```python
# backie/task.py
import abc
import json
import uuid

from .broker import Broker

class BaseTask(abc.ABC):
    """
    Example Usage:
        class AdderTask(BaseTask):
            task_name = "AdderTask"
            def run(self, a, b):
                result = a + b
                return result

        adder = AdderTask()
        adder.delay(9, 34)
    """
    task_name = None

    def __init__(self):
        if not self.task_name:
            raise ValueError("task_name should be set")
        self.broker = Broker()

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        # put your business logic here
        raise NotImplementedError("Task `run` method must be implemented.")

    def delay(self, *args, **kwargs):
        try:
            task_id = str(uuid.uuid4())
            _task = {"task_id": task_id, "args": args, "kwargs": kwargs}
            serialized_task = json.dumps(_task)
            self.broker.enqueue(queue_name=self.task_name, item=serialized_task)
            print("task: {0} succesfully queued".format(task_id))
        except Exception:
            raise Exception("Unable to publish task to the broker.")
```



#### (B) Broker

- BaseTask 는 작업들(tasks)를 저장하는데 broker를 사용한다. 해당 broker를 구현하는 코드
- redis를 백업 broker/저장소로 사용(어떠한 저장소를 사용해도 상관없음. ex. 메모리, 데이터베이스, 파일 시스템 등)
- [celery에서 사용가능한 브로커](http://docs.celeryproject.org/en/latest/getting-started/brokers/)

```python
# backie/broker.py
import redis # pip install redis

class Broker:
    """
    use redis as our broker.
    This implements a basic FIFO queue using redis.
    """
    def __init__(self):
        host = "localhost"
        port = 6379
        password = None
        self.redis_instance = redis.StrictRedis(
            host=host, port=port, password=password, db=0, socket_timeout=8.0
        )

    def enqueue(self, item, queue_name):
        self.redis_instance.lpush(queue_name, item)

    def dequeue(self, queue_name):
        dequed_item = self.redis_instance.brpop(queue_name, timeout=3)
        if not dequed_item:
            return None
        dequed_item = dequed_item[1]
        return dequed_item
```



#### (c) Worker

- 작업이 broker으로부터 저장 되었을 때, 실제로 작업을 수행할 클래스(Worker)
- json 데이터를 받아 변환(deserialize)한 다음 작업의 run 메서드 실행

```python
# backie/worker.py
import json

class Worker:
    """
    Example Usage:
        task = AdderTask()
        worker = Worker(task=task)
        worker.start()
    """
    def __init__(self, task) -> None:
        self.task = task

    def start(self,):
        while True:
            try:
                _dequeued_item = self.task.broker.dequeue(queue_name=self.task.task_name)
                dequeued_item = json.loads(_dequeued_item)
                task_id = dequeued_item["task_id"]
                task_args = dequeued_item["args"]
                task_kwargs = dequeued_item["kwargs"]

                print("running task: {0}".format(task_id))
                self.task.run(*task_args, **task_kwargs)
                print("succesful run of task: {0}".format(task_id))
            except Exception:
                print("Unable to execute task.")
                continue       
```



### Usage

- bakie를 사용한 task 예제
- 이메일을 보내는 작업을 가정

```python
# ecommerce_tasks.py
from backie.task import BaseTask

# pip install requests
import requests

class EmailTask(BaseTask):
    """
    task to send email to customer after they have ordered.
    """

    task_name = "EmailTask"

    def run(self, order_id, email_address):
        # lets pretend httpbin.org is an email service provider
        url = "https://httpbin.org/{0}/{1}".format(order_id, email_address)
        print(url)
        response = requests.get(url, timeout=5.0)
        print("response:: ", response)


if __name__ == "__main__":
    order_id = "24dkq40"
    email_address = "example@example.org"
    email_task = EmailTask()
    email_task.delay(order_id, email_address)
```



- email_task를 수행하는 worker 실행

```python
# ecommerce_worker.py
from ecommerce_tasks import EmailTask

from backie.worker import Worker

if __name__ == "__main__":
    email_task = EmailTask()

    # run workers
    worker = Worker(task=email_task)
    worker.start()
                
```



- redis 실행
  - 작업을 등록하기 위해서는 redis 서버가 동작하고 있어야 함

```bash
docker run -p 6379:6379 redis:5.0-alpine
```

- task 실행

```bash
python ecommerce_tasks.py
```

- worker 실행

```bash
python ecommerce_worker.py
```





### Conclusion

- 백그라운 프로세스의 동작원리는 간단함
- task 인자를 string으로 바꾸고, 데이터 베이스에 해당 string을 저장하고, 실제로 수행하기 위해 데이터베이스로부터 string을 가져와 작업(task)를 수행하는 것