"""automate_2048.py
2048 게임 웹 페이지로 접속 해
게임 종료될 때까지 실행"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import time


url = "https://gabrielecirulli.github.io/2048/"
driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)
# redirect 될 때까지 wait
wait.until(EC.url_changes(url))
# game-container 생성될때까지 wait
wait.until(lambda x: x.find_element_by_class_name("game-container"))

html_elem = driver.find_element_by_tag_name('html')
while True:
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)
    html_elem.send_keys(Keys.UP)

    try:
        driver.find_element_by_css_selector('.game-over')
    except Exception:
        pass
    else:
        break
