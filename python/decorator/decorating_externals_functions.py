import time
import numpy as np


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f'Function took {end-start}s')

        return ret

    return wrapper


rng = np.random.RandomState(0)

# Create a lot of numbers
nums = rng.random(10000000)
# Decorate np.sort with our time_it transformer
timed_sort = time_it(np.sort)
# Perform the sort with our time_it functionality
timed_sort(nums)