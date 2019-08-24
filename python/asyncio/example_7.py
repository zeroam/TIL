"""
example_7.py

Just a short example demonstrating a simple state machine in Python
This version is doing actual work, downloading the contents of
URL's it gets from a work_queue. This version uses the Twisted
framework to provide the concurrency
"""

from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor, task

import queue
import time


@defer.inlineCallbacks
def my_tasks(name, work_queue):
    try:
        while not work_queue.empty():
            url = work_queue.get()
            print(f'Task {name} getting URL: {url}')
            start_time = time.time()
            yield getPage(url)
            print(f'Task {name} got URL: {url}')
            print(f'Task {name} total elapsed time: {time.time() - start_time:.1f}')
    except Exception as e:
        print(str(e))


def main():
    """
    This is the main entry pointer for the program
    """
    # create the work_queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the work_queue
    for url in [
        b'http://google.com',
        b'http://yahoo.com',
        b'http://linkedin.com',
        b'http://shutterfly.com',
        b'http://mypublisher.com',
        b'http://facebook.com'
    ]:
        work_queue.put(url)

    # run the tasks
    start_time = time.time()
    defer.DeferredList([
        task.deferLater(reactor, 0, my_tasks, 'One', work_queue),
        task.deferLater(reactor, 0, my_tasks, 'Two', work_queue),
    ]).addCallback(lambda _: reactor.stop())

    # run the event loop
    reactor.run()

    print()
    print(f'Total elapsed time: {time.time() - start_time:.1f}')


if __name__ == '__main__':
    main()
