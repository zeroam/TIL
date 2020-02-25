def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)


def test_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    compare = factorial(n)
    print(f'{n}! = {compare}')
    assert result == compare, f'Wrong answer in {n}!'


if __name__ == '__main__':
    for i in range(10):
        test_factorial(i)