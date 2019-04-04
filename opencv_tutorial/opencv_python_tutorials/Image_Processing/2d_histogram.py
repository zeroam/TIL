# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:10:35 2019

@author: jone
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/2d_histogram.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0,180,0,256])

plt.figure(figsize=(8,6))
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(hist, interpolation='nearest'), plt.title('Hist')
plt.show()