from pathlib import Path

path = Path('C:/Users/imdff/Downloads')

print(f'{path}의 부모 디렉터리는 {path.parent}')
print(f'{path}의 부모의 부모 디렉터리는 {path.parent.parent}')

print(f'{path}의 모든 부모 디렉터리는 {list(path.parents)}')