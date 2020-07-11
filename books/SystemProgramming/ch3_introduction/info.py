"""info.py
platform 모듈을 이용한 시스템 정보 확인
"""
#!/usr/bin/env python
import sys
import platform
import multiprocessing

print(f"운영체제: {platform.system()}")
print(f"운영체제의 상세정보: {platform.platform()}")
print(f"운영체제 버전: {platform.version()}")
print(f"프로세서: {platform.processor()}")
print(f"CPU 수: {multiprocessing.cpu_count()}")
print(f"파이썬 버전: {sys.version}")
