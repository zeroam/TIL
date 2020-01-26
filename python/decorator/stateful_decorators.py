import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        print(f'Call {wrapper.num_calls} of {func.__name__!r}')
        return func(*args, **kwargs)

    wrapper.num_calls = 0
    return wrapper


@count_calls
def say():
    print('Hello')


say()
say()
say()
say()
print(say.num_calls)