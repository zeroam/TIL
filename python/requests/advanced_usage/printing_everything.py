import requests
from requests_toolbelt.utils import dump


def logging_hook(response, *args, **kwargs):
    data = dump.dump_all(response)
    print(data.decode('utf-8'))


http = requests.Session()
http.hooks['response'] = [logging_hook]

http.get('https://api.openaq.org/v1/cities', params={'country': 'BA'})
