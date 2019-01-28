# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 00:31:41 2018
Problem 2
- Even Fibonacci numbers
@author: zeroam
"""

def fibonacci(limit):
    first = 1
    second = 2
    cur = 0
    total = 2
    while cur < limit:
        if(cur%2 == 0):
            total += cur
        cur = first + second
        first = second
        second = cur
    return total

if __name__ == "__main__":
    print(fibonacci(4000000))