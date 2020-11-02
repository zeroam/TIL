import os
import requests
import bs4


url = "https://comic.naver.com/webtoon/detail.nhn?titleId=733766&no=37&weekday=mon"
resp = requests.get(url)
resp.raise_for_status()

soup = bs4.BeautifulSoup(resp.text, "html.parser")
img_list = soup.select("div.wt_viewer > img")

src_url = img_list[0].get("src")
print(src_url)
res = requests.get(url)
image_file = open("image/test.jpg", "wb")
image_file.write(res.content)
image_file.close()

dir = "image"
# os.makedirs(dir, exist_ok=True)
# for img in img_list:
#     url = img.get("src")
#     res = requests.get(url)

#     image_file = open(os.path.join(dir, os.path.basename(url)), "wb")
#     for chunk in res.iter_content(100000):
#         image_file.write(chunk)
#     image_file.close()
