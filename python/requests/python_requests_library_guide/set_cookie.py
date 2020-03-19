import requests

s = requests.Session()

# 쿠키값 sessionkie를 123456789으로 설정
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# 내 쿠키값 가져오기
r = s.get('https://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
