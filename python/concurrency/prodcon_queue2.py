import logging
import random
import concurrent.futures
import threading
import queue
import time

def producer(queue, event):
    """Pretent we're getting a number from the networ."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer get message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")


def consumer(queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Customer storing message: %s (size=%d}",
        message, queue.qsize())

    logging.info("Consumer received event. Exiting")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()