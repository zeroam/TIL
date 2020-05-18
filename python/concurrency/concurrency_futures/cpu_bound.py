import hashlib
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from utils import timeit


def hash_one(n):
    """A somewhat CPU-intensive task."""

    for i in range(1, n):
        hashlib.pbkdf2_hmac("sha256", b"password", b"salt", i * 1000)

    return "done"


@timeit
def hash_all(n):
    """Function that does hashing in serial."""

    for _ in range(n):
        hash_one(n)

    return "done"


@timeit
def hash_all_multithread(n):

    with ThreadPoolExecutor(max_workers=6) as executor:
        for arg, res in zip(range(n), executor.map(hash_one, range(n))):
            pass

    return "done"


@timeit
def hash_all_multiprocess(n):

    with ProcessPoolExecutor(max_workers=6) as executor:
        for arg, res in zip(range(n), executor.map(hash_one, range(n))):
            pass

    return "done"


if __name__ == "__main__":
    size = 50
    hash_all(size)
    hash_all_multithread(size)
    hash_all_multiprocess(size)
