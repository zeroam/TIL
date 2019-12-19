from pathlib import Path
from os import chdir

path = Path('..')

print(f'현재 작업 디렉터리: {path.cwd()}')

# 디렉터리 이동
chdir(path)

print(f'현재 작업 디렉터리: {path.cwd()}')

chdir('..')