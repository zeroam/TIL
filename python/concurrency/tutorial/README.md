# Concurrency

### 참조링크

- [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)





<hr>

# Thread

### 참조링크

- [An Intro to Threading in Python](<https://realpython.com/intro-to-python-threading/>)



- 스레드는 개별적인 실행 흐름이다.
  - 한번에 두가지 이상의 것들을 할 수 있음
  - 실제로 두가지 이상 하는 것은 아님
  - 실제로 2가지 이상의 실행을 하려면 multoprocessing을 사용해야 함
- 스레드가 모든 프로그램의 성능을 좋게하는 것은 아님
  - 대기 작업이 많은 프로그램의 경우 성능의 이점이 있음
  - CPU 성능을 많이 사용하는 프로그램의 경우 성능의 이점이 없음



#### 데몬스레드

- 컴퓨터 과학에서 데몬스레드는 background에서 동작하는 프로세스

- 데몬스레드는 프로그램이 끝날때 즉시 종료됨(동작중이더라도)

- 파이썬 스레드는 기본적으로 데몬스레드가 아님

  - `x = threading.Thread(target=thread_function, args=(1,), daemon=True)`
  - daemon 인자값에 True를 줌으로써 데몬스레드로 생성 가능

- 결과값 비교

  - 데몬스레드는 Thread1: finishing이 호출되기전에 프로그램이 종료됨
  - 스레드의 join() 메소드로 이 문제를 해결

  ```bash
  # 파이썬 일반 스레드
  $ ./single_thread.py
  Main    : before creating thread
  Main    : before running thread
  Thread 1: starting
  Main    : wait for the thread to finish
  Main    : all done
  Thread 1: finishing
  
  # 데몬스레드
  $ ./daemon_thread.py
  Main    : before creating thread
  Main    : before running thread
  Thread 1: starting
  Main    : wait for the thread to finish
  Main    : all done
  
  # join 메소드 활용
  $ ./daemon_thread.py
  Main    : before creating thread
  Main    : before running thread
  Thread 1: starting
  Main    : wait for the thread to finish
  Thread 1: finishing
  Main    : all done
  ```

  

#### 여러 스레드 사용하기

- join 메소드 활용

```python
# multiple_threads.py
import logging
import threading
import time


def thread_function(name):
    logging.info(f'Thread {name}: starting')
    time.sleep(2)
    logging.info(f'Thread {name}: finishing')

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info(f"Main     : create and start thread {index}")
        x = threading.Thread(target=thread_function, args=(index, ))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info(f"Main     : before joining thread {index}")
        thread.join()
        logging.info(f"Main     : thread {index} done")
```



- ThreadPoolExecutor 사용
  - thread를 start 하거나 join 할 필요 없음
  - with 블록이 .join()의 역할

```python
# executor.py
import logging
import time
import concurrent.futures


def thread_function(name):
    logging.info(f'Thread {name}: starting')
    time.sleep(2)
    logging.info(f'Thread {name}: finishing')

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
```



#### Race Conditions

- Race conditions는 두개 이상의 스레드가 공유된 자원이나 데이터에 접근할 때 발생함.

  - 이러한 문제는 아주 사소한 것이 될 수 있으며, 디버그를 어렵게 하는 요인이다.

- 예제

  - 2가 출력되어야 하지만 1이 출력됨
  - Thread1, 2 모두 self.value가 업데이트 되기전의 값인 0을 참조해서 업데이트 하기때문에 이러한 오류가 생김

  ```python
  # racecond.py
  import time
  import logging
  import concurrent.futures
  
  class FakeDatabase:
      def __init__(self):
          self.value = 0
  
      def update(self, name):
          logging.info(f'Thread {name}: starting update')
          local_copy = self.value
          local_copy += 1
          time.sleep(0.1)
          self.value = local_copy
          logging.info(f'Thread {name}: finishing update')
  
  if __name__ == "__main__":
      format = "%(asctime)s: %(message)s"
      logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
  
      database = FakeDatabase()
      logging.info(f"Testing update. Starting value is {database.value}")
      with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
          for index in range(2):
              executor.submit(database.update, index)
      logging.info(f"Testing update. Ending value is {database.value}")
  
  ```

#### Lock을 사용한 동기화

- race conditions를 해결하기 위해 Lock을 사용함

  - 하나의 스레드만 Lock에 접근할 수 있음
  - 다른 언어에서는 mutex라고도 불림

- .acquire(), .realease()를 사용

  - acquire() 된 자원은 다른 스레드가 접근할 수 없으며, 다른 스레드는 이 자원이 release() 될 때까지 기다림
  - 만일 하나의 스레드가 acquire() 한 채로 release()를 하지 않는다면 프로그램은 stuck이 됨

- with 명령어로 acquire(), release()를 자동으로 호출할 수 있음

- 예제

  ```python
  # fixrace.py
  import time
  import logging
  import threading
  import concurrent.futures
  
  class FakeDatabase:
      def __init__(self):
          self.value = 0
          self._lock = threading.Lock()
  
      def update(self, name):
          logging.info(f'Thread {name}: starting update')
          logging.debug(f'Thread {name} about to lock')
          with self._lock:
              logging.debug(f'Thread {name} has lock')
              local_copy = self.value
              local_copy += 1
              time.sleep(0.1)
              self.value = local_copy
              logging.debug(f'Thread {name} about to release lock')
          logging.debug(f'Thread {name} after release')
          logging.info(f'Thread {name}: finishing update')
  
  if __name__ == "__main__":
  
      format = "%(asctime)s: %(message)s"
      logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
      logging.getLogger().setLevel(logging.DEBUG)
  
      database = FakeDatabase()
      logging.info(f"Testing update. Starting value is {database.value}")
      with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
          for index in range(2):
              executor.submit(database.update, index)
      logging.info(f"Testing update. Ending value is {database.value}")
      
  ```

  

#### Deadlock

- Lcoks를 사용할 때 발생할 수 있는 문제

  - acquire이 두번 호출 되었을 때, Lock이 release 될 때까지 계속 기다리고 있어 프로그램이 끝나지 않는 상태

  ```python
  # deadlock.py
  import threading
  
  l = threading.Lock()
  print('before first acquire')
  l.acquire()
  print('before second acquire')
  l.acquire()
  print('acquire lock twice')
  ```

  

#### Producer-Consumer Threading

- Producer-Consumer Problem : 프로세스 동기화나 스레딩에서 나타날 수 있는 문제
  - bounded-buffer problem이라고도 불림
  - 문제는 꽉찬 버퍼에 더 이상 데이터를 넣지 않도록 하고, 빈 버퍼에 더 이상 데이터를 제거하지 않도록 하는 것



- Producer-Consumer Using Lock

  - acquire, release를 사용함으로써 문제해결
  - 좋은 해결방법은 아님, 한 번에 1개의 값만 허락하기 때문

  ```python
  # prodcon_lock.py
  import logging
  import random
  import concurrent.futures
  import threading
  
  SENTINEL = object()
  
  class Pipeline:
      """
      Class to allow a single element pipeline between producer and consumer
      """
      def __init__(self):
          self.message = 0
          self.producer_lock = threading.Lock()
          self.consumer_lock = threading.Lock()
          self.consumer_lock.acquire()
  
      def get_message(self, name):
          logging.debug(f"{name}: about to acquire getlock")
          self.consumer_lock.acquire()
          logging.debug(f"{name}: have getlock")
          message = self.message
          logging.debug(f"{name}: about to release setlock")
          self.producer_lock.release()
          logging.debug(f"{name}: setlock released")
          return message
  
      def set_message(self, message, name):
          logging.debug(f"{name}: about to acquire setlock")
          self.producer_lock.acquire()
          logging.debug(f"{name}: have setlock")
          self.message = message
          logging.debug(f"{name}: about to release getlock")
          self.consumer_lock.release()
          logging.debug(f"{name}: getlock released")
  
  
  def producer(pipeline):
      """Pretend we're getting a message from the network."""
      for index in range(10):
          message = random.randint(1, 101)
          logging.info(f"Producer got message: {message}")
          pipeline.set_message(message, "Producer")
  
      # Send a sentinel message to tell consumer we're done
      pipeline.set_message(SENTINEL, "Producer")
  
  
  def consumer(pipeline):
      """Pretend we're saving a number in the database."""
      message = 0
      while message is not SENTINEL:
          message = pipeline.get_message("Consumer")
          if message is not SENTINEL:
              logging.info(f"Consumer storing message: {message}")
  
  if __name__ == "__main__":
      format = "%(asctime)s: %(message)s"
      logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
      #logging.getLogger().setLevel(logging.DEBUG)
  
      pipeline = Pipeline()
      with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
          executor.submit(producer, pipeline)
          executor.submit(consumer, pipeline)
  ```

  



- Producer-Consumer Using Queue
  - 파이프라인에서 1개 이상의 값을 다루고 싶을 때 사용