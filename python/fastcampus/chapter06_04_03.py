"""파이썬 심화
Asyncio
비동기 I/O Coroutine 작업
- Generator -> 반복적인 객체 Return(yield)
- 즉, 실행 stop -> 다른 작업으로 위임 -> stop 지점부터 재실행 원리
- Non-Blocking 비동기 처리에 적합
"""

# BlockIO -> Thread 사용
# 쓰레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결
import asyncio
import timeit
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from urllib.request import urlopen

urls = [
    "http://daum.net",
    "https://google.com",
    "https://tistory.com",
    "https://github.com",
    "https://gmarket.co.kr",
]


async def fetch(url, executor):
    print("Thread Name:", threading.current_thread().getName(), "start", url)
    res = await loop.run_in_executor(executor, urlopen, url)
    print("Thread Name:", threading.current_thread().getName(), "done", url)
    return res.read()[0:5]


async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # asyncio.ensutre_future
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    rst = await asyncio.gather(*futures)

    print("Result: ", rst)


if __name__ == "__main__":
    start = timeit.default_timer()

    # 루프 생성
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print("Total Time", duration)
