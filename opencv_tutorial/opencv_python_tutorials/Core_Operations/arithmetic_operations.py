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

# Numpy - modulo 연산
img = img1 + img2
cv2.imshow('img', img)
cv2.waitKey(0)

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