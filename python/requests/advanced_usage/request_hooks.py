import requests

http = requests.Session()

assert_status_hook = lambda response, *args, **kwargs: response.raise_for_status()
http.hooks['response'] = [assert_status_hook]

# requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.github.com/user/repos?page=1
resp = http.get('https://api.github.com/user/repos?page=1')
print(resp)