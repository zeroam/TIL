"""image_site_downloader.py
imgur에서 특정 키워드로 검색한 이미지 다운로드
"""
import os
import bs4
import requests

url = "https://imgur.com/search"


def get_img_elements(query):
    resp = requests.get(url, params=[("q", query)])
    resp.raise_for_status()

    soup = bs4.BeautifulSoup(resp.text, "lxml")
    img_elemns = soup.select(".image-list-link img")

    return img_elemns


def save_file(img_url: str, dir_name: str):

    if not img_url.startswith('http'):
        img_url = f"https:{img_url}"

    print(f"Downloading {img_url}")
    resp = requests.get(img_url)
    resp.raise_for_status()

    with open(os.path.join(dir_name, os.path.basename(img_url)), 'wb') as f:
        for chunk in resp.iter_content(100000):
            f.write(chunk)


def main():
    # TEMP variable
    dir_name = 'imgur'
    search_query = "car"

    img_elemns = get_img_elements(search_query)

    os.makedirs(dir_name, exist_ok=True)
    for elem in img_elemns:
        save_file(elem.get('src'), dir_name)


if __name__ == "__main__":
    main()
