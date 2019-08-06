def file_read():
    with open('words.txt') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.rstrip('\n')


def is_prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def prime_number_generator(start, stop):
    for i in range(start, stop + 1):
        if is_prime(i):
            yield i


start, stop = 950, 1000
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
