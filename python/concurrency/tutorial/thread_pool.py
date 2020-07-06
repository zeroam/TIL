# thread_pool.py
import sys
from queue import Queue
from threading import Thread


class Worker(Thread):
    """큐로부터 주어진 작업을 실행하는 스레드"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kwargs = self.tasks.get()
            try:
                func(*args, **kwargs)
            except Exception as e:
                # 스레드에서 에러 발생
                print(e)
            finally:
                # 에러가 발생했던, 하지 않았던 완료 시키기
                self.tasks.task_done()


class ThreadPool:
    """큐로부터 작업을 소비(consume)하는 스레드들의 Pool"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kwargs):
        """큐에 작업 추가"""
        self.tasks.put((func, args, kwargs))

    def map(self, func, args_list):
        """작업 리스트 큐에 추가"""
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """큐의 모든 작업이 완료될 때까지 대기"""
        self.tasks.join()


if __name__ == "__main__":
    from random import randrange
    from time import sleep

    # 스레드에서 실행되는 함수
    def wait_delay(d):
        print(f"sleeping for {d}sec")
        sleep(d)

    # 랜덤으로 delay 생성
    delays = [randrange(3, 7) for i in range(50)]

    # 5개의 worker를 가진 스레드 풀 생성
    pool = ThreadPool(5)

    pool.map(wait_delay, delays)
    pool.wait_completion()
