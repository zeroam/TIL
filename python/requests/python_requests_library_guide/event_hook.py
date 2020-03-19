import requests

def print_url(r, *args, **kwargs):
	print(r.url)


def record_hook(r, *args, **kwargs):
    r.hook_called = True


response = requests.get('https://httpbin.org/', 
                        hooks={'response': [print_url, record_hook]})
print(response.hook_called)
