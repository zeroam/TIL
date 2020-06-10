"""submitting_forms.py"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://login.metafilter.com")

# id가 user_name인 태그 검색 후 문자열 입력
user_elem = browser.find_element_by_id("user_name")
user_elem.send_keys("your_read_username_here")

# id가 user_pass인 태그 검색 후 문자열 입력
password_elem = browser.find_element_by_id("user_pass")
password_elem.send_keys("your_real_password_here")
password_elem.submit()
