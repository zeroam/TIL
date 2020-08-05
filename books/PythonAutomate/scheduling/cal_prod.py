"""cal_prod.py
10만번 곱한 시간 측정
"""
import time


def cal_prod():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


if __name__ == "__main__":
    start_time = time.time()
    prod = cal_prod()
    end_time = time.time()

    print(f"The result is {len(str(prod))} digits long")
    print(f"Took {end_time - start_time} seconds to calculate")
