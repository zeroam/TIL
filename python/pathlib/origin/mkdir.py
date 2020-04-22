import os
from pathlib import Path

dir_name = 'new'
# os.path를 이용한 디렉터리 생성
path = os.path.join(os.getcwd(), dir_name)
os.mkdir(path)

# pathlib.Path를 이용한 디렉터리 생성
path = Path.cwd() / dir_name
path.mkdir()