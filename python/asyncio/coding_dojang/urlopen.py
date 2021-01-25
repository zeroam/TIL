from time import time
from urllib.request import Request, urlopen

urls = [
    "https://www.google.com/search?q=" + i
    for i in ["apple", "pear", "grape", "pineapple", "orange", "strawberry", "pie", "helloworld"]
]

begin = time()
result = []
for url in urls:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(request)
    page = response.read()
    result.append(len(page))

print(result)
end = time()
print(f"실행 시간: {end - begin:.3f}초")
