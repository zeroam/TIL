from concurrent.futures import ThreadPoolExecutor


def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function
    print(f.result())


with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(wait_on_future)
    print(future.result())
