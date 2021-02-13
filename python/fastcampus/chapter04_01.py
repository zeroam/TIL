"""
파이썬 함수 특징
1. 런타임 초기화
2. 변수 등에 할당 가능
3. 함수 인수 전달 가능
4. 함수 결과로 반환 가능
"""

# function vs class
def factorial(n: int) -> int:
    """Factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(factorial.__code__)
print(sorted(set(dir(factorial)) - set(dir(A))))
print()


# assign to variable
func_var = factorial

print(func_var)
print(func_var(5))
print(map(func_var, range(1, 6)))
print(list(map(func_var, range(1, 6))))
print()


# pass function to parameter or return function
print(list(map(func_var, filter(lambda x : x % 2 == 1, range(1, 6)))))
print([func_var(i) for i in range(1, 6) if i % 2 == 1])
print()


# reduce
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(reduce(lambda x, y: x + y, range(1, 11)))  # lambda, 가급적 주석 사용, 가급적 함수 사용
print(sum(range(1, 11)))
print()


# Callable
import random

# 로또 추첨 클래스 선언
class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for _ in range(6)])

    def __call__(self):
        return self.pick()


game = LottoGame()

print(callable(str), callable(list), callable(factorial), callable(3.14))
print(callable(game))
print(game.pick())
print(game())
print()


# 함수 Signature
from inspect import signature

sg = signature(add)
print(sg)
print(sg.parameters)

for name, param in sg.parameters.items():
    print(name, param.kind, param.default)
print()


# Partial 사용법 : 인수 고정 -> 주로 특정 인수 고정 후 콜백함수에 사용
from operator import mul
from functools import partial

five = partial(mul, 5)
six = partial(five, 6)

print(mul(5, 500))
print(five(100))
print([five(i) for i in range(1, 11)])
print(six())
