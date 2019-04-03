# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:09:48 2019

@author: jone
"""

#%% Hierarchy
import cv2
import random

img = cv2.imread('img/contour_hierarchy.png')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 125, 255, 0)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('original', img)
cv2.waitKey(0)

for cnt in contours:
    # Random Color 생성
    b = random.randint(1, 255)
    g = random.randint(1, 255)
    r = random.randint(1, 255)
    
    img = cv2.drawContours(img, [cnt], -1, (b,g,r), 2)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()