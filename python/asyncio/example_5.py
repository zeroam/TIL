"""
example_5.py

Just a short example demonstrating a simple state machine in Python
This version is doing actual work, downloading the contents of
URL's it gets from a queue
"""

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
        yield


def main():
    """
    This is the main entry point for program
    """

    # create the queue of 'work'
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

    tasks = [
        task('One', work_queue),
        task('Two', work_queue)
    ]
    # run the scheduler to run the tasks
    start_time = time.time()
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

    print()
    print(f'Total elapsed time: {time.time() - start_time:.1f}')


if __name__ == '__main__':
    main()