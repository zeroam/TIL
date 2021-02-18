"""파이썬 심화
흐름제어, 병행처리(Concurrency)
제너레이터, 반복형
"""
# 제너레이터

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# 반복 가능한 이유? iter(x) 함수 호출
from collections import abc


t = "ABCDEF"

# for 문 사용
for c in t:
    print(c, end=", ")
print()

# while 문 사용
w = iter(t)
while True:
    try:
        print(next(w), end=", ")
    except StopIteration:
        break
print()

# 반복형 확인
print(hasattr(t, "__iter__"))
print(isinstance(t, abc.Iterable))
print()

# next 사용
class WordSplitIter(object):
    def __init__(self, text):
        self._text = text
        self._idx = 0

    def __next__(self):
        print("called __next__")
        try:
            word = self._text[self._idx]
            self._idx += 1
        except IndexError:
            # 초기화 필요
            self._idx = 0
            raise StopIteration
        return word

    def __iter__(self):
        print("called __iter__")
        return self

    def __repr__(self):
        return f"WordSplitIter '({self._text})'"


wi = WordSplitIter("ITERATOR")
print(next(wi))
for c in wi:
    print(c, end=", ")
print()
for c in wi:
    print(c, end=", ")
print()


# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가될 경우 메모리 사용량 증가 -> 제너레이터 완화
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3. 딕셔너리, 리스트 한 번 호출할 때 마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 함

class WordSplitGenerator(object):
    def __init__(self, text):
        self._text = text
        self._idx = 0

    def __iter__(self):
        print("called __iter__")
        for word in self._text:
            yield word

    def __repr__(self):
        return f"WordSplitGenerator '({self._text})'"


wg = WordSplitGenerator("GENERATOR")
wg_iter = iter(wg)
print(wg_iter)
print(next(wg_iter))
for c in wg:
    print(c, end=", ")
print()
print()


# Generator ex 1
def generator_ex1():
    print("START")
    yield "AAA"
    print("CONTINUE")
    yield "BBB"
    print("END")

temp = generator_ex1()
print(next(temp))
print(next(temp))
# print(next(temp))  # StopIteration
print()

for c in generator_ex1():
    print(c)


# Generator ex 2
temp2 = [x * 3 for x in generator_ex1()]
print(temp2)
temp3 = (x * 3 for x in generator_ex1())
print(temp3)
for i in temp3:
    print(i)
print()


# Generator ex 3
import itertools

gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print()


def gen1_impl(start, interval):
    cur = start
    while True:
        yield cur
        cur += interval
gen1_1 = gen1_impl(1, 2.5)
print(next(gen1_1))
print(next(gen1_1))
print(next(gen1_1))
print(next(gen1_1))
print()

# 조건
gen2 = itertools.takewhile(lambda n: n < 50, itertools.count(1, 2.5))
for num in gen2:
    print(num, end=", ")
print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])
for num in gen3:
    print(num, end=", ")
print()

# 누적합계
gen4 = itertools.accumulate(range(10))
for num in gen4:
    print(num, end=", ")
print()
