import time


def countup(n):
    while True:
        n += 2
        yield n


def countdown(n):
    while True:
        n = n - 1
        yield n



def main(n):
    while True:
        n = next(countup(n))
        print(n)
        time.sleep(0.5)
        n = next(countdown(n))
        print(n)
        time.sleep(0.5)


if __name__ == "__main__":
    main(0)