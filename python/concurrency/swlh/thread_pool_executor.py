import concurrent.futures
import urllib.request
from time import sleep

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        if url == 'http://www.cnn.com/':
            sleep(10)
        return conn.read()


if __name__ == '__main__':
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f'{url} generated an exception: {exc}\n')
            else:
                print(f'{url} page size is {len(data)} bytes')
