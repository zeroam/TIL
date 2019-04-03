# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:43:54 2019

@author: jone
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/lightning.png')
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 125, 255, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

# 끝점 좌표 찾기
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

# 좌표 표시하기
points = [leftmost, rightmost, topmost, bottommost]
for point in points:
    cv2.circle(img1, point, 20, (0,0,255), -1)
    
img1 = cv2.drawContours(img1, cnt, -1, (255, 0, 0), 5)

titles = ['Original', 'Result']
images = [img, img1]

plt.figure(figsize=(8, 4))

for i in range(2):
    plt.subplot(1, 2, i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()