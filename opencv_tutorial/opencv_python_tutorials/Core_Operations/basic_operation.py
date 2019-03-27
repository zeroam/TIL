# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:25:37 2019

@author: jone
"""
#%% Image ROI
import cv2

img = cv2.imread('baseball-player.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)

# img[행의 시작점: 행의 끝점, 열의 시작점: 열의 끝점]
ball = img[435:480, 817:884]
img[490:535, 817:884] = ball # 다른 영역에 paste
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Splitting and Merging Image Channel
import cv2

img = cv2.imread('baseball-player.jpg')

# 채널 분리 및 합치기
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))
cv2.imshow('img', img)
cv2.waitKey(0)

# Numpy indexing
r,g,b = img[:,:,0], img[:,:,1], img[:,:,2]
img = cv2.merge((b,g,r))
cv2.imshow('img', img)
cv2.waitKey(0)

img[:,:,0] = 0 # Blue 색 제거
cv2.imshow('img', img)
cv2.waitKey(0)


cv2.destroyAllWindows()

#%% Making Borders for Images
import cv2
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('opencv_logo.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL'), plt.axis('off')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE'), plt.axis('off')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT'), plt.axis('off')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101'), plt.axis('off')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP'), plt.axis('off')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT'), plt.axis('off')

plt.show()