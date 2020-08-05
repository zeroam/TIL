# run_basic.py
from tasks import add

task1 = add.delay(2, 5)
task2 = add.apply_async(args=[4, 2])
task3 = add.apply_async(kwargs={"x": 3, "y": 6})

print(" 작업 ID 조회 ".center(50, "="))
print(f"  task1: {task1.id}")
print(f"  task2: {task2.id}")
print(f"  task3: {task3.id}")

print(" 작업 완료여부 조회 ".center(50, "="))
print(f"  task1: {task1.ready()}")
print(f"  task2: {task2.ready()}")
print(f"  task3: {task3.ready()}")

print(" 결과 데이터 조회 (완료될때까지 Pause) ".center(50, "="))
print(f"  task1: {task1.get()}")
print(f"  task2: {task2.get()}")
print(f"  task3: {task3.get()}")

print(" 작업 완료여부 조회 ".center(50, "="))
print(f"  task1: {task1.ready()}")
print(f"  task2: {task2.ready()}")
print(f"  task3: {task3.ready()}")
