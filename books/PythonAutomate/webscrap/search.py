"""search.py
인자값을 전달한 키워드 기반으로 상위 n개 링크
웹 브라우저 실행"""
import sys
import requests, webbrowser, bs4


URLS = {
    'google': 'https://google.com/search?q=',
    'duckduckgo': 'https://duckduckgo.com/?q='
}


def parse_args() -> list:
    if len(sys.argv) < 2:
        print(f'python {__file__} <search query>')
        sys.exit(1)
    
    return sys.argv[1:]


def get_http_resp(query, url):
    print('Searching...')

    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(f'{url}{query}', headers=headers)
    resp.raise_for_status()

    return resp


def find_google_elems(resp):
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    link_elemns = soup.select('.r > a')

    return link_elemns


def get_duckduckgo_resp(resp):
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    link_elemns = soup.select('.result__a')

    return link_elemns


def main():
    args = parse_args()
    query = ' '.join(args).replace(' ', '+')

    resp = get_http_resp(query, URLS['google'])
    link_elemns = find_google_elems(resp)

    num_open = min(5, len(link_elemns))
    index = 0
    while index < num_open:
        href = link_elemns[index].get('href')
        print(href)
        if href.startswith('http'):
            webbrowser.open(link_elemns[index].get('href'))
        index += 1


if __name__ == "__main__":
    main()
