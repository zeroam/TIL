# 'yield from' can be used to delegate iteration


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def countup(stop):
    n = 1
    while n < stop:
        yield n
        n += 1


def up_and_down(n):
    yield from countup(n)
    yield from countdown(n)


if __name__ == "__main__":
    for x in up_and_down(3):
        print(x)
