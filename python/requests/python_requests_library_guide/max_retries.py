import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

http_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# 해당 url로 접근할 때 adapter를 적용시킨다.
session.mount('https://', http_adapter)
session.mount('https://api.github.com', http_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
