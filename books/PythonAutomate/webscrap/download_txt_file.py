import requests

# 웹으로부터 텍스트 파일 요청
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

# Response 객체 반환
print(type(res))

# 응답 결과가 성공적인지 출력
print(res.status_code == requests.codes.ok)

# 응답 결과가 정상적이지 않으면 에러 발생
res.raise_for_status()

# 텍스트 파일의 길이 출력
print(len(res.text))

# 파일에 저장
with open("RomeoAndJuliet.txt", "wb") as f:
    # 한번에 너무 많은 메모리를 사용하는 것 방지
    for chunk in res.iter_content(100000):
        f.write(chunk)