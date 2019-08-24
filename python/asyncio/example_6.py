"""
example_6.py

Just a short example demonstrating a simple state machine in Python
This version is doing actual work, downloading the contents of
URL's it gets from a queue. It's also using gevent to get the 
URL's in an asynchronous manner.
"""

import gevent
from gevent import monkey
monkey.patch_all()

import queue
import requests
import time


def task(name, work_queue):
    while not work_queue.empty():
        url = work_queue.get()
        print(f'Task {name} getting URL: {url}')
        start_time = time.time()
        requests.get(url)
        print(f'Task {name} got URL: {url}')
        print(f'Task {name} total elapsed time: {time.time() - start_time:.1f}')


def main():
    """
    This is the main entry for the program
    """
    # Create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for url in [
        'http://google.com',
        'http://yahoo.com',
        'http://linkedin.com',
        'http://shutterfly.com',
        'http://mypublisher.com',
        'http://facebook.com'
    ]:
        work_queue.put(url)

    # run the tasks
    start_time = time.time()

    tasks = [
        gevent.spawn(task, 'One', work_queue),
        gevent.spawn(task, 'Two', work_queue)
    ]
    gevent.joinall(tasks)
    print()
    print(f'Total elapsed time: {time.time() - start_time:.1f}')


if __name__ == '__main__':
    main()