# run_group.py
from tasks import add
from celery import group

# task signature 생성
sigs = [add.s(i, i + 1) for i in range(5)]

# group signature 생성
job = group(sigs)
print(f"group: {job}")

res = job()

print(" 작업 조회 ".center(50, "="))
print(f"  task id: {res.id}")
print(f"  result type: {type(res)}")

print(" 상태 조회 ".center(50, "="))
print(f"  task ready: {res.ready()}")

print(" 결과 반환 ".center(50, "="))
print(f"  task completed: {res.completed_count()}")  # 완료한 subtask 갯수 출력
print(f"  task results: {res.get()}")
print(f"  task results: {res.join()}")  # 호출한 순서대로 리턴
print(f"  task completed: {res.completed_count()}")

print(" 상태 조회 ".center(50, "="))
print(f"  task ready: {res.ready()}")
print(f"  task successful: {res.successful()}")  # 모든 작업이 성공적으로 완료되었는 지
