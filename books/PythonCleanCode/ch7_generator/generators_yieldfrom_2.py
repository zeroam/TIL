"""Clean Code in Python - Chapter 7: Using Generators

> yield from: Capture the return value.
"""

from log import logger


def sequence(name, start, end):
    logger.info("%s started at %i", name, start)
    yield from range(start, end)
    logger.info("%s finished at %i", name, end)
    return end


def main():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)
    return step1 + step2


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)

    g = main()

    for _ in range(10):
        print(next(g))

    try:
        print(next(g))
    except StopIteration as e:
        print(f"return value: {e}")
