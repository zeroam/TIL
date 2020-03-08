"""피보나치 수열 Memoization"""
def fib_memo(n, cache):
    if n < 3:
        return 1
    
    if n in cache:
        return cache[n]

    cache[n] = fib_memo(n - 2, cache) + fib_memo(n - 1, cache)

    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


if __name__ == '__main__':
    assert fib(10) == 55, 'fib(10) error'
    assert fib(50) == 12586269025, 'fib(50) error'
    assert fib(100) == 354224848179261915075, 'fib(100) error'