import time
import pyautogui
import random

time_interval = 5

while True:
    time.sleep(time_interval)
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    pyautogui.move(x, y, duration=0.25)
