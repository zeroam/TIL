import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=['HEAD', 'GET', 'OPTIONS'],
    backoff_factor=1
)

adapter = HTTPAdapter(max_retries=retry_strategy)

http = requests.Session()
http.mount('https://', adapter)
http.mount('http://', adapter)

response = http.get('https://en.wikipedia.org/w/api.php')
print(response)
