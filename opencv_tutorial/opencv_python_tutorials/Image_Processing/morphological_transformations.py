# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:18:39 2019

@author: jone
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/morph.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

# erosion : 침식, dilation : 확장
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)

# opening : erosion -> dilation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing : dilation -> erosion
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# gradient : dilation과 erosion의 차이
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# tophat : opening과 원본의 차이
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# blackhat : closing과 원본의 차이
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]
titles = ['image', 'erosion', 'dilation', 'opening', 'closing', 'gradient', 'tophat', 'blackhat']

# plt 사이즈 조정
plt.figure(figsize=(8, 6))

for i in range(len(images)):
    plt.subplot(3, 3, i+1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
