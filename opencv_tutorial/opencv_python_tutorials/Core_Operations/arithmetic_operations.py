# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:50:57 2019

@author: jone
"""
#%% Image Addition
import cv2

img1 = cv2.imread('img/flower1.jpg')
img2 = cv2.imread('img/flower2.jpg')

cv2.imshow('img', img1)
cv2.waitKey(0)
cv2.imshow('img', img2)
cv2.waitKey(0)

# cv2.add() - Saturation 연산
img = cv2.add(img1, img2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite('img/flower_saturation.jpg', img)

# Numpy - modulo 연산
img = img1 + img2
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite('img/flower_modulo.jpg', img)

cv2.destroyAllWindows()

#%% Image Blending
import cv2

img1 = cv2.imread('img/flower1.jpg')
img2 = cv2.imread('img/flower2.jpg')

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('W', 'image', 0, 100, nothing)

while True:
    w = cv2.getTrackbarPos('W', 'image')
    dst = cv2.addWeighted(img1, float(100-w) * 0.01, img2, float(w)* 0.01, 0)
    cv2.imshow('image', dst)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()

#%% Bitwise Operations
import cv2
import numpy as np

img1 = cv2.imread('img/opencv_logo.png')
img2 = cv2.imread('img/lena.jpg')

# 사빕할 이미지의 row, col, channel 정보
rows, cols, channels = img1.shape

# 대상 이미지에서 삽입할 이미지의 영역을 추출
roi = img2[0:rows, 0:cols]

# mask를 만들기 위해서 img1을 gray로 변경후 binary image로 변환
# mask는 logo부분이 흰색(255), 바탕은 검은색(0)
# mask_inv는 logo부분이 검은색(0), 바탕은 흰색(255)
img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

cv2.imshow('image', mask)
cv2.waitKey(0)
cv2.imshow('image', mask_inv)
cv2.waitKey(0)

# bitwise_and 연산자는 둘다 0이 아닌 경우만 값을 통화시킴
# 즉 mask가 검정색이 아닌 경우만 통과가 되지 때문에 mask영역 이외는 모두 제거됨.
# 아래 img1_fg의 경우는 bg가 제거되고 fg(logo부분)만 남게됨
# img2_bg는 roi영역에서 logo부분이 제거되고 bg만 남게됨
img1_fg = cv2.bitwise_and(img1, img1, mask=mask)
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

cv2.imshow('image', img1_fg)
cv2.waitKey(0)
cv2.imshow('image', img2_bg)
cv2.waitKey(0)

# 2개의 이미지를 합치면 바탕은 제거되고 logo부분만 합쳐짐
dst = cv2.add(img1_fg, img2_bg)

# 합쳐진 이미지를 원본에 추가
img2[0:rows, 0:cols] = dst

cv2.imshow('res', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.destroyAllWindows()