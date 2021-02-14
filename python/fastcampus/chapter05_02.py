"""
파이썬 클래스 특별 메소드 심화 활용 및 상속
class ABC
"""
class VectorP(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return (i for i in (self.__x, self.__y))  # Generator

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = float(v)

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, v):
        if v < 30:
            raise ValueError("Below 30 is not allowed")
        self.__y = float(v)


v = VectorP(20, 40)

# Iter
for val in v:
    print(val, end=", ")
print()

# ValueError
try:
    v = VectorP(20, 20)
except ValueError as e:
    print(e)
print()


# 객체 슬라이싱
class Objects(object):
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]

s = Objects()
print(len(s))
print(len(s._numbers))
print(s[1])
print(s[1:10])
print()


# 파이썬 추상 클래스
# https://docs.python.org/3/library/collections.abc.html
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으올 작성하게 하는 것

# Sequence 상속받지 않았지만 자동으로 __iter__, __contains__ 기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜
class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]


it1 = IterTestA()
print(it1[2])
print(it1[1:10])
print(5 in it1)
print([x for x in it1])
print()


# Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작
from collections.abc import Sequence


class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])


it2 = IterTestB()
print(it2[2])
print(it2[1:10])
print(5 in it2)
print([x for x in it2])
print()


import abc


class RandomMachine(abc.ABC):
    @abc.abstractmethod
    def load(self, iterobj):
        """Iterable 항목 추가"""

    @abc.abstractmethod
    def pick(self):
        """무작위 항목 뽑기"""

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        return tuple(sorted(items))


import random


class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Empty Crane Box")

    def __call__(self):
        return self.pick()


# 서브 클래스 확인
print(issubclass(CraneMachine, RandomMachine))
print(CraneMachine.__mro__)
print()

cm = CraneMachine(range(30, 50))
print(cm._items)
print(cm.pick())
print(cm())
print(cm.inspect())

