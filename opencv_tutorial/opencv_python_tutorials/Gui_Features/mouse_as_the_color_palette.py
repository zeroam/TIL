# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:24:57 2019

@author: jone
"""
#%% Simple Demo
import cv2
import numpy as np

# callback 함수
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
        
# 빈 이미지 생성
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()

#%% Advanced Demo
import cv2
import numpy as np

drawing = False     # Mouse가 클릭된 상태 확인
mode = True         # True이면 사각형, False면 원
ix, iy = -1, -1

# mouse callback 함수
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스를 누른 상태
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동
        if drawing == True:     # 마우스를 누른 상태일 경우
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
            
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):   # 사각형, 원 Mode 변경
        mode = not mode
    elif k == 27:       # Esc 누르면 종료
        break
    
cv2.destroyAllWindows()