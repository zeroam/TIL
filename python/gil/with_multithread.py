from time import time
from threading import Thread


def factorize(number):
    for i in range(1, number + 1):
        if number % 1 == 0:
            yield i


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


numbers = [8402868, 2295738, 5938342, 7925426]
start = time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

# wait for all thread to finish
for thread in threads:
    thread.join()
end = time()
print(f'Took {end - start:.3f} seconds')

