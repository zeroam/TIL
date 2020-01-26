import functools


class ClassDecorator(object):
    def __init__(self, arg1, arg2):
        print(f'Arguments of decorators {arg1}, {arg2}')
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        functools.update_wrapper(self, func)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


@ClassDecorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
        print(arg)


print_args(1, 2, 3)