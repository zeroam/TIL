"""Clean Code in Python - Chapter 7: Using Generators

> yield from: send values & throw exceptions

"""
from log import logger


class CustomException(Exception):
    """A type of exception that is under control."""


def sequence(name, start, end):
    value = start
    logger.info("%s started at %i", name, value)
    while value < end:
        try:
            received = yield value
            logger.info("%s received %r", name, received)
            value += 1
        except CustomException as e:
            logger.info("%s is handling %s", name, e)
            received = yield "OK"
    return end


def main():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)
    return step1 + step2


if __name__ == "__main__":
    g = main()

    # step1
    print(next(g))  # 0
    print(next(g))  # 1
    print(g.send("첫 번째 제너레이터를 위한 인자 값"))  # 2
    print(g.throw(CustomException("처리 가능한 예외 던지기")))  # OK
    print(next(g))  # 2
    print(next(g))  # 3
    print(next(g))  # 4

    # step2
    print(next(g))  # 5
    print(g.throw(CustomException("두 번째 제너레이터를 위한 예외 던지기")))  # OK
