# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:42:42 2019

@author: jone
"""

#%% 기본 임계처리
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/squirrel.jpg', 0)

# 사이즈 조정
h, w = img.shape
r = 300/w
dim = (int(r*w), int(r*h))
img_resize = cv2.resize(img, dim)

cv2.imshow('img', img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


ret, thresh1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO_INV)

titles =['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

#%% 적응 임계처리
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/squirrel.jpg', 0)
# img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

titles = ['Original', 'Global', 'Mean', 'Gaussian']

images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
