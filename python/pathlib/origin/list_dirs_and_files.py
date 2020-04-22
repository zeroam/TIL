from pathlib import Path

path = Path('C:/Users/imdff/Documents')

dirs = [e for e in path.iterdir() if e.is_dir()]
print(f'디렉터리 목록: {dirs}')

files = [e for e in path.iterdir() if e.is_file()]
print(f'파일 목록: {files}')