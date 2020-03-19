import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """커스텀 인증 클래스 구현"""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """API 토큰을 헤더에 추가한다"""
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r

print(requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token')))
