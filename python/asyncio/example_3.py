"""
example_3.py

Just a short example demonstrating a simple state machine in Python
However, this one has delays that affect it
"""

import time
import queue


def check_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(f'Task {args[0]} total elapsed time: {time.time() - start_time:.1f}')
    return wrapper


def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        start_time = time.time()
        for x in range(count):
            print(f'Task {name} running')
            time.sleep(1)
            total += 1
            yield
        print(f'Task {name} total: {total}')
        print(f'Task {name} total elapsed time: {time.time() - start_time:.1f}')



def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

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
    print(f'Task elapsed time: {time.time() - start_time:.1f}')

if __name__ == '__main__':
    main()