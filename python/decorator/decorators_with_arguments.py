import functools


def repeat(*args_, **kwargs_):
    def inner_function(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(args_[0]):
                func(*args, **kwargs)
        return wrapper
    return inner_function


@repeat(4)
def say(name):
    print(f'Hello {name}')


say('World')