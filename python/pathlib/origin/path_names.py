from pathlib import Path

path = Path('C:/Users/imdff/Downloads')

print(path)
# file:/// 으로 시작하는 표기방식으로 출력
print(path.as_uri())
# 디렉터리 구분이 \ 가 아닌 /으로 출력
print(path.as_posix())