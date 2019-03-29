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
