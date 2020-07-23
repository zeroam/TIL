"""convert_date.py
파이썬 포맷 변환 예제
"""
from datetime import datetime

# 파이썬 날짜 데이터를 지정된 포맷의 문자열 데이터로 변환
oct_21th = datetime(2020, 10, 21, 17, 30, 5)
print(oct_21th.strftime("%Y/%m/%d %H:%M:%S"))  # 2020/10/21 17:30:05
print(oct_21th.strftime("%I:%M %p"))  # 05:30 PM
print(oct_21th.strftime("%B of %y"))  # October of 20

# 지정된 포맷의 문자열 데이터를 파이썬 날짜 데이터로 변환
dateformat = "October 21, 2020"
print(datetime.strptime(dateformat, "%B %d, %Y"))
dateformat = "2020/10/21 17:30:05"
print(datetime.strptime(dateformat, "%Y/%m/%d %H:%M:%S"))
dateformat = "October of 20"
print(datetime.strptime(dateformat, "%B of %y"))
