def fib_optimized(n):
    if n in [1, 2]:
        return 1

    previous = 1
    current = 1
    for _ in range(3, n + 1):
        result = previous + current

        previous = current
        current = result

    return result


if __name__ == '__main__':
    assert fib_optimized(10) == 55, 'fib(10) error'
    assert fib_optimized(50) == 12586269025, 'fib(50) error'
    assert fib_optimized(100) == 354224848179261915075, 'fib(100) error'