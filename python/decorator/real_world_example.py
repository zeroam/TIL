import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finised {repr(func.__name__)} in {run_time:.3f}')
        return value

    return wrapper


@timer
def doubled_and_add(num):
    res = sum([i * 2 for i in range(num)])
    print(f'Result : {res}')

doubled_and_add(100000)
doubled_and_add(1000000)