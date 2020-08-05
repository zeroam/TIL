"""datetime_sample.py
datetime 모듈 활용
"""
import time
from datetime import datetime, timedelta

# 현재 시간 출력
print(f"현재시간: {datetime.now()}")

# 지정한 시간 출력
print(f"지정한 시간: {datetime(2019, 2, 27, 11, 10, 49, 0)}")

# 시간 속성 값 접근
dt = datetime.now()
print(f"년: {dt.year}, 월: {dt.month}, 일: {dt.day}")
print(f"시: {dt.hour}, 분: {dt.minute}, 초: {dt.second}")

# UNIX 시간으로부터 현재 날짜 얻기
unix_time = time.time()
print(f"UNIX 시간: {unix_time}, 날짜: {datetime.fromtimestamp(unix_time)}")

# 시간 비교
today = datetime(2020, 7, 22)
same_day = datetime(2020, 7, 22)
yesterday = datetime(2020, 7, 21)
print(f"today == same_day : {today == same_day}")
print(f"today == yester_day : {today == yesterday}")
print(f"today > yester_day : {today > yesterday}")

# timedelta를 이용해 시간 연산하기
dt = datetime.now()
thousand_says = dt + timedelta(days=1000)
print(f"1000일 후 : {thousand_says}")

# 특정일자(5초 뒤) 까지 기다리기
dt = datetime.now()
five_seconds = timedelta(seconds=5)
print("before 5 seconds")
while datetime.now() < dt + five_seconds:
    time.sleep(1)
print("after 5 seconds")
