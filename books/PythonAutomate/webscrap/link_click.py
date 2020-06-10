"""link_click.py"""
from selenium import webdriver

# 브라우저 실행 (chromedriver 가 PATH에 설정되어 있어야 함)
browser = webdriver.Chrome()
# inventwithpython.com 접속
browser.get('https://inventwithpython.com')

# 클래스명이 'cover-thumb' 인 태그 찾기
try:
	elem = browser.find_element_by_class_name('cover-thumb')
	print(f"Found {elem.tag_name} element with that class name!")
except:
	print("Was not able to find an element with that name")

# text가 'Read Online for Free'인 링크를 검색 후 클릭
link_elem = browser.find_element_by_link_text("Read Online for Free")
type(link_elem)  # selenium.webdriver.remote.webelement.WebElement
link_elem.click()