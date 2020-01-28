from time import time
from multiprocessing import Process


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def main():
    numbers = [8402868, 2295738, 5938342, 7925426]
    start = time()
    processes = []
    for number in numbers:
        process = Process(target=factorize, args=(number,))
        process.start()
        processes.append(process)

    # wait for all thread to finish
    for p in processes:
        p.join()
    end = time()
    print(f'Took {end - start:.3f} seconds')


if __name__ == '__main__':
    main()