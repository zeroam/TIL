from pathlib import Path

path = Path('C:/Users/imdff/Documents/Python Scripts')

# .py으로 끝나는 파일
for e in path.rglob('*.py'):
    print(e)

# .py으로 끝나는 파일 - 하위 폴더까지 조회
for e in path.rglob('**/*.py'):
    print(e)