# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:39:00 2019

@author: jone
"""

import cv2
import numpy as np

def nothing(x):
    pass

# 검은 바탕화면의 윈도우 창 생성
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# trackbar를 생성하여 named window에 등록
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

# On/Off 스위치 생성
switch = '0:OFF\1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    # trackbar의 현재 위치 받기
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
        
cv2.destroyAllWindows()