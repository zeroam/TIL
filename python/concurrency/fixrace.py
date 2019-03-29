import time
import logging
import threading
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info(f'Thread {name}: starting update')
        logging.debug(f'Thread {name} about to lock')
        with self._lock:
            logging.debug(f'Thread {name} has lock')
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug(f'Thread {name} about to release lock')
        logging.debug(f'Thread {name} after release')
        logging.info(f'Thread {name}: finishing update')

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    database = FakeDatabase()
    logging.info(f"Testing update. Starting value is {database.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info(f"Testing update. Ending value is {database.value}")
    