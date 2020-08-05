import time
import pyautogui

# 주 모니터 사이즈 얻기
screen_width, screen_height = pyautogui.size()

"""마우스"""
current_mouse_x, current_mouse_y = pyautogui.position()  # 마우스 X, Y 좌표 얻기
pyautogui.moveTo(100, 150, duration=0.25)  # 마우스 이동 0.25초 동안 이동
pyautogui.click()  # 마우스 클릭
pyautogui.click(100, 200, duration=1)  # 마우스 좌표 1초 동안 이동 후 클릭
pyautogui.click(500, 300, button="right", duration=0.25)  # 마우스 오른쪽 버튼 클릭
pyautogui.click(500, 300, button="left", duration=0.25)  # 마우스 왼쪽 버튼 클릭
pyautogui.click("help_icon.png")  # help_icon.png 파일을 스크린 상에서 찾아 클릭

# 상대 좌표 이동
for i in range(3):
    pyautogui.move(100, 0, duration=0.25)  # 오른쪽
    pyautogui.move(0, 100, duration=0.25)  # 아래
    pyautogui.move(-100, 0, duration=0.25)  # 왼쪽
    pyautogui.move(0, -100, duration=0.25)  # 위

# 마우스 끌기
pyautogui.click()  # 현재 윈도우창 활성화
distance = 200
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)  # 오른쪽
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)  # 아래
    pyautogui.drag(-distance, 0, duration=0.2)  # 왼쪽
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # 위

# 마우스 스크롤 (양수: 올리기, 음수: 내리기)
pyautogui.scroll(-100)

"""키보드"""
pyautogui.write("Hello world!", interval=0.25)  # 각각의 문자마다 0.25초 간격으로 입력
pyautogui.press("esc")  # Esc 입력, 키 명칭은 pyautogui.KEY_NAMES에 있음

pyautogui.keyDown("shift")  # shift 키 누른 상태로 유지
pyautogui.press(["left", "left", "left", "left"])  # 왼쪽 화살표 키 4번 입력
pyautogui.keyUp("shift")  # shift 키 떼기

pyautogui.hotkey("ctrl", "c")  # Ctrl-C hotkey 조합 입력

pyautogui.alert("This is the message to display.")  # 경고창 띄우고 OK 누를 때 까지 프로그램 중지
