"""gui_screen.py
화면 관련 작업 진행하기
"""
import pyautogui

# 스크린샷 찍기 (이미지 객체 불러오기)
im = pyautogui.screenshot()

# 픽셀 RGB 값 가져오기
print(pyautogui.pixel(0, 0))

try:
    # 이미지 인식
    loc = pyautogui.locateOnScreen("help_icon.png")  # 좌표 얻기, 없으면 Error
    print(f"loc: {loc}, left: {loc.left}")

    # 이미지 인식 - 리스트 반환 (2개 이상 매칭이 필요할 때)
    locs = pyautogui.locateAllOnScreen("help_icon.png")
    print(list(locs))

except Exception:
    print("Image coult not found.")
