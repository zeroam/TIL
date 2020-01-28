import threading


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(sensor_index, items, counter):
    for _ in range(items):
        # Read from the sensor
        # ...
        counter.increment()


def run_threads(func, items, counter):
    threads = []
    for i in range(5):
        args = (i, items, counter)
        thread = threading.Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    items = 100000
    counter = Counter()
    run_threads(worker, items, counter)
    print(f'Counters should be {5 * items}, found {counter.count}')

