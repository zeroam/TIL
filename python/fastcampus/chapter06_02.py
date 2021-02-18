"""파이썬 심화
흐름제어, 병행처리(Concurrency)
yield
코루틴 (Coroutine)
"""

# yield : 메인루틴 <-> 서브루틴
# 코루틴 제어, 코루틴 상태, 양방향값 제어
# yield from

# 서브루틴 : 메인루틴에서 -> 리턴에 의해 호출부분으로 돌아와 다시 프로세스
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 틀정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아가 수행가능 -> 동시성 프로그래밍 가능
# 코루틴 : 코루틴 스케쥴링 오버헤드 매우 적다
# 스레드 : 싱글 스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가

# Coroutine ex 1
def coroutine1():
    print(">>> coroutine started")
    i = yield
    print(f">>> coroutine received: {i}")


c1 = coroutine1()
print(c1, type(c1))

# yield 실행 전까지 진행
next(c1)

# 기본으로 None 전달
# next(c1)

# 값 전송
# c1.send(100)

# 잘못된 사용
c2 = coroutine1()
# c2.send(100)
print()


# 코루틴 예제
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태
from inspect import getgeneratorstate


def coroutine2(x):
    print(f">>> coroutine started: {x}")
    y = yield x
    print(f">>> coroutine received: {y}")
    z = yield x + y
    print(f">>> coroutine received: {z}")

c3 = coroutine2(10)
print(getgeneratorstate(c3))
print(next(c3))
print(getgeneratorstate(c3))
print(c3.send(15))
print(getgeneratorstate(c3))
# print(c3.send(15))  # 예외
print()


# 데코레이터 패턴
from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def sumer():
    temp = 0
    total = 0
    while True:
        temp = yield total
        total += temp

c4 = sumer()
print(c4.send(20))
print(c4.send(30))
print(c4.send(40))
print()


# 코루틴 예제 3 - 예외 처리
class SampleException(Exception):
    """설명에 사용할 예외 처리"""


def coroutine_exe():
    print(">>> coroutine started")
    while True:
        try:
            x = yield
        except SampleException:
            print(">>> SampleException handled. continue")
        else:
            print(f">>> coroutine received: {x}")


exe_co = coroutine_exe()
next(exe_co)  # coroutine start
exe_co.send(10)
exe_co.send(20)
exe_co.throw(SampleException)
exe_co.send(30)
exe_co.close()  # GEN_CLOSED
# exe_co.send(10)  # StopIteration 예외 발생
print()


# 코루틴 예제 4 - 결과값 반환
def coroutine_return():
    print(">>> coroutine started")
    total = 0
    cnt = 0
    while True:
        x = yield
        if x is None:
            break
        total += x
        cnt += 1

    print(">>> coroutine ended")
    return f"Avg: {total / cnt}"


ret_co = coroutine_return()
next(ret_co)
ret_co.send(50)
ret_co.send(60)
ret_co.send(70)
try:
    ret_co.send(None)
except StopIteration as e:
    print(e.value)
print()


# 코루틴 예제 5 - yield from
# StopIteration 자동처리 (3.7 -> await)
# 중첩 코루틴 처리
def gen1():
    for c in "AB":
        yield c
    for n in range(2, 5):
        yield n

t1 = gen1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
t2 = gen1()
print(list(t2))
print()


def gen2():
    yield from "AB"
    yield from range(2, 5)

t3 = gen2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
t4 = gen2()
print(list(t4))
print()


def gen3_sub():
    print("Sub coroutine.")
    x = yield 10
    print(f"Recv: {x}")
    x = yield 100
    print(f"Recv: {x}")


def gen4_main():
    print(">>> main coroutine start")
    yield from gen3_sub()
    print(">>> main coroutine end")
    yield


t5 = gen4_main()
print(next(t5))
print(t5.send(7))
print(t5.send(77))
