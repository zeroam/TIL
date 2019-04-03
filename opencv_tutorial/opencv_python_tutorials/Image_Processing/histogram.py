# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:45:55 2019

@author: jone
"""

#%% Histogram in OpenCV
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('img/flower1.jpg', 0)
img2 = cv2.imread('img/flower2.jpg', 0)

hist1 = cv2.calcHist([img1], [0], None, [256], [0,256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0,256])

plt.figure(figsize=[8,6])
plt.subplot(221), plt.imshow(img1, 'gray'), plt.title('Red Line')
plt.subplot(222), plt.imshow(img2, 'gray'), plt.title('Green Line')
plt.subplot(223), plt.plot(hist1, color='r'), plt.plot(hist2, color='g')
plt.xlim([0,256])
plt.show()

#%% Mouse Position
import cv2

def print_pos(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x, y:', x, y)

img = cv2.imread('img/hand.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image', print_pos)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break



#%% Histogram Mask
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/hand.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# mask 생성
mask = np.zeros(img.shape[:2], np.uint8)
cv2.rectangle(mask, (150, 100), (450, 350), (255, 255, 255), -1)

# 이미지에 mask가 적용된 결과
masked_img = cv2.bitwise_and(img, img, mask=mask)

# 원본 이미지의 히스토그램
hist_full = cv2.calcHist([img], [1], None, [256], [0,256])

# mask를 적용한 히스토그램
hist_mask = cv2.calcHist([img], [1], mask, [256], [0,256])

plt.figure(figsize=(8,6))

plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.subplot(222), plt.imshow(mask, 'gray'), plt.title('Mask')
plt.subplot(223), plt.imshow(masked_img, 'gray'), plt.title('Masked Image')

# red는 원본 이미지 히스토그램, blue는 mask 적용된 히스토그램
plt.subplot(224), plt.title('Histogram')
plt.plot(hist_full, color='r'), plt.plot(hist_mask, color='b')
plt.xlim([0, 256])

plt.show()
