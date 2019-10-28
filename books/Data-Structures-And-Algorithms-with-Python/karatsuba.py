import math
from math import log10


def karatsuba(x, y):
    # The best case for recursion
    if x < 10 and y < 10:
        return x * y

    # sets n, number of digits in the highest input number
    n = max(int(log10(x) + 1), int(log10(y) + 1))

    # rounds up n/2
    n_2 = int(math.ceil(n/2.0))
    # adds 1 if n is uneven
    n = n if n % 2 == 0 else n + 1
    # splits the input numbers
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)
    # applies the three recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac - bd

    # performs the multiplication
    return ((10**n) * ac + (10**n_2) * ad_bc + bd)


if __name__ == '__main__':
    t = karatsuba(1234, 5678)
    print(t)