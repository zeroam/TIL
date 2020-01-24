import time 

def isPrime(n):
    for num in range(2, n//2):
        if n%num == 0:
            return False
    return True


def kth_prime(k):
    candidate = 2
    while k:
        if isPrime(candidate):
            k -= 1
        candidate += 1
    return candidate - 1


# Driver code
start = time.time()
print(kth_prime(10000)) # The 10000th prime number is 104723
end = time.time()
print(f'{end - start:.2f} seconds collapsed')