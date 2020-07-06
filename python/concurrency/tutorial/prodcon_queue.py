# prodcon_queue.py
import logging
import random
import concurrent.futures
import threading
import queue
import time

class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug("%s: about to get from queue", name)
        value = self.get()
        logging.debug("%s: got %d from queue", name, value)
        return value

    def set_message(self, value, name):
        logging.debug("%s: about to add %d to queue", name, value)
        self.put(value)
        logging.debug("%s: added %d to queue", name, value)


def producer(pipeline, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    logging.info("Producer received EXIT event. Exiting")


def consumer(pipeline, event):
    """Pretend we're saving a number in the database."""
    # event가 set() 되지 않거나 파이프라인에 데이터가 있으면 종료되지 않음
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s (queue size=%d)",
            message, pipeline.qsize(),
        )
    
    logging.info("Consumer received EXIT event. Exiting")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
