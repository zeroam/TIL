def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def Primes(max_):
    number = 1
    generated = 0
    while generated < max_:
        number += 1
        if check_prime(number):
            generated += 1
            yield number


if __name__ == '__main__':
    prime_generator = Primes(100)

    for x in prime_generator:
        print(x)