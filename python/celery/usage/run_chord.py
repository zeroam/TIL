# run_chord.py
from celery import chord

from tasks import add, tsum

# task signature 생성
sigs = [add.s(i, i + 1) for i in range(5)]

c = chord(sigs)
res = c(tsum.s())

print(" 작업 조회 ".center(50, "="))
print(f"  task id: {res.id}")
print(f"  result type: {type(res)}")

print(" 상태 조회 ".center(50, "="))
print(f"  task ready: {res.ready()}")

print(" 결과 반환 ".center(50, "="))
print(f"  task results: {res.get()}")

print(" 상태 조회 ".center(50, "="))
print(f"  task ready: {res.ready()}")
