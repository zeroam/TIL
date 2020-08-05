# run_chain.py
from tasks import add
from celery import chain

# task signature 생성
sig1 = add.s(3, 5)
sig2 = add.s(8)
sig3 = add.s(2)

# chain signature 생성
sig_chain = chain(sig1, sig2, sig3)
print(f"chain: {sig_chain}")

# 비동기 작업 실행
res = sig_chain()

print(" 작업 ID 조회 ".center(50, "="))
print(f"  chain: {res.id}")

print(" 작업 완료여부 조회 ".center(50, "="))
print(f"  chain: {res.ready()}")

print(" 결과 데이터 조회 (완료될때까지 Pause) ".center(50, "="))
print(f"  chain: {res.get()}")

print(" 작업 완료여부 조회 ".center(50, "="))
print(f"  chain: {res.ready()}")
