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