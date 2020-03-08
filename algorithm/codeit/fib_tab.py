"""피보나치 수열 Tabulation"""
def fib_tab(n):
    table = [0, 1, 1]

    for i in range(3, n + 1):
        table.append(table[i - 2] + table[i - 1])

    return table[n]


if __name__ == '__main__':
    assert fib_tab(10) == 55, 'fib(10) error'
    assert fib_tab(50) == 12586269025, 'fib(50) error'
    assert fib_tab(100) == 354224848179261915075, 'fib(100) error'
