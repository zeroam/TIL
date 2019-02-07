import requests
from bs4 import BeautifulSoup


def parse_image(data):
    soup = BeautifulSoup(data, 'html.parser')
    imgTagList = soup.find_all('img')
    dataSet = set(x.attrs['src'] for x in imgTagList)
    return dataSet


def main():
    url = "http://www.google.co.kr"

    res = requests.get(url)
    charset = res.encoding
    data = res.content.decode(charset)

    dataSet = parse_image(data)
    print("\n>>>>>>>>>> Fetch Images from", url)
    print("\n".join(sorted(dataSet)))


if __name__ == "__main__":
    main()