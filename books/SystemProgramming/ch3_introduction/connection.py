#!/usr/bin/env python
import os

from settings import MANAGEMENT_SERVER, SERVER1, SERVER2

print("어떤 파이썬 서버에 연결하시겠습니까?")
select = input("연결하고자 하는 파이썬 서버를 선택하세요(m, 1, 2) : ")

if select == "m":
    os.system(f"ssh jone@{MANAGEMENT_SERVER}")
elif select == "1":
    os.system(f"ssh jone@{SERVER1}")
elif select == "2":
    os.system(f"ssh jone@{SERVER2}")
else:
    print("잘못 선택하셨습니다")
