def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper


def hello():
    print('hello')


def world():
    print('world')


trace_hello = trace(hello)
trace_hello()
trace_world = trace(world)
trace_world()
