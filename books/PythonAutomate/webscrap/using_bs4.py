import bs4

with open("example.html") as f:
    # 텍스트 파일로 부터 BeautifulSoup 객체 생성
    soup = bs4.BeautifulSoup(f.read(), "lxml")

print(type(soup))  # <class 'bs4.BeautifulSoup'>

# id가 author인 태그 리스트 조회
elems = soup.select("#author")
print(type(elems))  # <class 'list'>
print(type(elems[0]))  # <class 'bs4.element.Tag'>

# 태그를 포함한 문자열 출력
print(str(elems[0]))

# 태그 안의 텍스트만 출력
print(elems[0].getText())

# 태그의 속성값 출력
print(elems[0].attrs)

# 해당 태그의 id값 조회
print(elems[0].get('id'))
