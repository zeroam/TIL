import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    print(b.result())
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())
    return 6


with ThreadPoolExecutor(max_workers=2) as executor:
    # here, the future from a depends on the future from b
    # and vice versa
    # so this is never going to be completed
    a = executor.submit(wait_on_b)
    b = executor.submit(wait_on_a)

    print("Result from wait_on_b", a.result())
    print("Result from wait_on_a", b.result())
