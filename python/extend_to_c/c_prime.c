#include <stdio.h>
#include "primeheader.h"

int isPrime(int n) {
    for (int i = 2; i < n/2; i++) {
        if (n%i == 0) {
            return 0;
        }
    }
    return 1;
}


int kthPrime(int k) {
    int candidate = 2;
    while (k) {
        if (isPrime(candidate)) {
            k--;
        }
        candidate++;
    }
    return candidate - 1;
}

// Driver code
int main() {
    printf("%d\n", kthPrime(10000));
    return 0;
}