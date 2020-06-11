"""link_click.py - 링크확인
웹페이지의 URL이 주어지면 그 페이지에 링크된 모든 페이지를 다운로드
"""
import argparse
import os
import requests
from urllib import parse
from bs4 import BeautifulSoup


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url path")
    parser.add_argument("-d", "--dir", default="link", help="directory path")

    args = parser.parse_args()
    return args


def main(args):
    url = args.url
    dir_path = args.dir
    invalid_urls = [None, "#", "/"]

    resp = requests.get(url)
    resp.raise_for_status()
    os.makedirs(dir_path, exist_ok=True)

    soup = BeautifulSoup(resp.text, "lxml")
    links = soup.select("a")
    hrefs = []
    for link in links:
        href = link.get("href")
        if href in invalid_urls:
            continue

        # set relative url path to absolute url path
        if not href.startswith("http"):
            href = parse.urljoin(url, href)

        # checking duplicates
        if href in hrefs:
            # print(f"{href} already downloaded")
            continue

        try:
            sub_resp = requests.get(href)
            if sub_resp.status_code == requests.codes.ok:
                print(f"Writing: {href}")
                base_name, *ext = os.path.basename(href).split(".")
                base_name = base_name + ".html"
                with open(os.path.join(dir_path, base_name), "wb") as f:
                    for chunk in resp.iter_content(100000):
                        f.write(chunk)
            else:
                print(f" ERROR(status:{sub_resp.status_code}) ".center(30, "-"))
                print(f"  link: {href}")
                print("-" * 30)
        except Exception as e:
            print(f" Exception ".center(30, "="))
            print(f"  {e}")
            print("=" * 30)

        hrefs.append(href)


if __name__ == "__main__":
    args = parse_args()
    main(args)
