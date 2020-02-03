import time
import random
from threading import Thread


class Worker(Thread):
    def __init__(self, number):
        Thread.__init__(self)
        self._number = number

    def run(self):
        sleep = random.randrange(1, 10)
        time.sleep(sleep)
        print(f'Worker {self._number}, slept for {sleep} seconds')


if __name__ == '__main__':
    for i in range(1, 6):
        task = Worker(i)
        task.start()

    print('Total 5 Threads are queued, let\'s see when they finished!')
