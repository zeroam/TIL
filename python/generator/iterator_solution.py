def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


class Primes:
    def __init__(self, max_):
        # the maximum number of primes we want generated
        self.max = max_
        # start with this number to check if it is prime
        self.number = 1
        # No of primes generated yet. We want to StopIteration when
        # it reaches max
        self.primes_generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.primes_generated >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            self.primes_generated += 1
            return self.number
        else:
            return self.__next__()


if __name__ == '__main__':
    prime_generator = Primes(100)

    for x in prime_generator:
        print(x)