"""socket_module_sample.py
도메인 이름에 대한 IP 정보 확인하기
"""
#!/usr/bin/env python
import socket

host = socket.gethostbyname_ex("www.google.com")

print(" HOST 정보를 출력 ".center(40, "="))
print(host)
print()

print(" HOST 정보를 한 줄씩 출력 ".center(40, "="))
for i in host:
    print(i)
print()

print(" HOST 정보를 한 줄씩 출력 ".center(40, "="))
hostname, aliaslist, ipaddrlist = host
print(f"ip : {ipaddrlist[0]}")
