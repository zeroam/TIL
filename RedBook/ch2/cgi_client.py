from urllib.request import urlopen
from urllib.parse import urlencode

url = 'http://127.0.0.1:8888/cgi-bin/script.py'
data = {
    'name': '김석훈',
    'email': 'shkim@naver.com',
    'url': 'http://www.naver.com',
}
encData = urlencode(data)
postData = encData.encode('ascii')

f = urlopen(url, postData) # POST
print(f.read().decode('cp949'))