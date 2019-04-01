# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:52:17 2019

@author: imdff
"""

#%% Image Filtering
import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('img/squirrel.jpg')

# 사이즈 조정
h, w = img.shape[:2]
r = 900/w
dim = (int(r*w), int(r*h))
img = cv2.resize(img, dim)

cv2.namedWindow('image')
cv2.createTrackbar('K', 'image', 1, 20, nothing)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('K', 'image')
    
    # (0, 0)이면 에러가 발생함으로 1로 치환
    if k == 0:
        k = 1
        
    # trackbar에 의해서 (1,1) ~ (20,20) kernel 생성
    kernel = np.ones((k,k), np.float32) / (k**2)
    dst = cv2.filter2D(img, -1, kernel)
    
    cv2.imshow('image', dst)
    
cv2.destroyAllWindows()

#%% Image Blurring
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/monkey.tiff')

# pyplot을 사용하기 위해 BGR을 RGB로 변환
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])

# 일반 Blur
dst1 = cv2.blur(img, (7,7))

# GaussianBlur
dst2 = cv2.GaussianBlur(img, (5,5), 0)

# Median Blur
dst3 = cv2.medianBlur(img, 9)

# Bilateral Filtering
dst4 = cv2.bilateralFilter(img, 9, 75, 75)

plt.figure(figsize=(16, 12))

images = [img, dst1, dst2, dst3, dst4]
titles = ['Original', 'Blur(7X7)', 'Gaussian Blur(5X5)', 'Median Blur', 'Bilateral']

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

#%% Image blurring 2
import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('trackbar')
cv2.createTrackbar('K', 'trackbar', 1, 20, nothing)

img = cv2.imread('img/squirrel.jpg')

# 사이즈 조정
h, w = img.shape[:2]
r = 500/w
dim = (int(r*w), int(r*h))
img = cv2.resize(img, dim)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('K', 'trackbar')
    
    if k == 0:
        k = 1
    elif k%2 == 0:
        k = k - 1
        
    dst1 = cv2.blur(img, (k, k))
    dst2 = cv2.GaussianBlur(img, (k, k), 0)
    dst3 = cv2.medianBlur(img, k)
    dst4 = cv2.bilateralFilter(img, k, 75, 75)
    
    cv2.imshow('image', img)
    cv2.imshow('blur', dst1)
    cv2.imshow('gaussian', dst2)
    cv2.imshow('median', dst3)
    cv2.imshow('bilateral', dst4)
    
cv2.destroyAllWindows()
