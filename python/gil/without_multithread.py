from time import time

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


numbers = [8402868, 2295738, 5938342, 7925426]
start = time()
for number in numbers:
    list(factorize(number))
end = time()

print(f'Took {end - start:.3f} seconds')