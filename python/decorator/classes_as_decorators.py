import functools


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Call {self.num_calls} of {self.func.__name__!r}')
        return self.func(*args, **kwargs)


@CountCalls
def say():
    print('Hello!')


say()
say()
say()
say()
print(say.num_calls)
