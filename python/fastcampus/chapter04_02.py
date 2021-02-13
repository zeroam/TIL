"""
일급 함수(일급 객체)
Decorator & Closure
"""
# 파이썬 변수 범위 (global)

# Closure (클로저)
# 반환되는 내부 함수에 대해서 선언 된 연결을 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다.

a = 10
print(a + 10)
print(a + 100)  # 결과를 누적할 수는 없을까?

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print(f"class >>> {self._series} / {len(self._series)}")
        return sum(self._series) / len(self._series)


avg_cls = Averager()
print(avg_cls(10))
print(avg_cls(10))
print(avg_cls(100))
print()


# 클로저(Closure) 사용 -> 함수의 실행이 끝나도 접근이 가능함
# 전역변수 사용 감소, 디자인 패턴 적용
# 많이 사용하면 리소스 많이 잡아먹을 수 있음
def closure_avg1():
    # Free variable
    series = []
    # 클로저 영역

    def averager(v):
        series.append(v)
        print(f"class >>> {series} / {len(series)}")
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_avg1()
print(avg_closure1(10))
print(avg_closure1(10))
print(avg_closure1(100))
print()

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))  # 함수 내부에서 리턴한 함수 -> 새로운 속성값들 생성됨
print()
print(avg_closure1.__code__.co_freevars)  # 클로저 영역안에 있는 변수
print()
print(dir(avg_closure1.__closure__[0]))
print()
print(dir(avg_closure1.__closure__[0].cell_contents))
print()


# 잘못된 클로저 사용 예
# imutable 객체를 클로저 영역에서 선언 후 별도 nonlocal 선언 없이 사용할 경우 예외 발생
def closure_avg2():
    # Free variable
    cnt = 0
    total = 0
    # 클로저 영역
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_avg2()

print(avg_closure2(10))
print(avg_closure2(10))
print(avg_closure2(100))
print()


# 데코레이터 실습
# 1. 중복 제거, 코드 간결
# 2. 클로저보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함
import time

def perf_clock(func):
    def wrapper(*args):
        st = time.perf_counter()
        result = func(*args)

        et = time.perf_counter() - st
        args_str = ",".join((repr(arg) for arg in args))
        print(f"[{et:0.5f}s {func.__name__}({args_str}) -> {result}")
        return result

    return wrapper


def time_func(seconds):
    time.sleep(seconds)


def sum_func(*numbers):
    return sum(numbers)


def factorial(n):
    return n * factorial(n - 1) if n > 2 else 1


# 데코레이터 미사용
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(factorial)

print(non_deco1, non_deco1.__code__.co_freevars)
print(non_deco2, non_deco2.__code__.co_freevars)
print(non_deco3, non_deco3.__code__.co_freevars)

non_deco1(1)
non_deco2(100, 200, 300, 400, 500)
non_deco3(50)
print()
