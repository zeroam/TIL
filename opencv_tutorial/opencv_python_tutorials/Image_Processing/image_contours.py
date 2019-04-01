# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:56:02 2019

@author: jone
"""

import cv2

def nothing(x):
    pass

img = cv2.imread('img/apple.jpg')

# 사이즈 조정
h, w = img.shape[:2]
r = 400/w
dim = (int(r*w), int(r*h))
img = cv2.resize(img, dim)

cv2.namedWindow('canny')
cv2.createTrackbar('K', 'canny', 80, 255, nothing)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('K', 'canny')
    
    canny = cv2.Canny(img, k, 3*k)

    image_external, contours_external, hierachy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_tree, contours_tree, hierachy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image_external = cv2.drawContours(img.copy(), contours_external, -1, (0, 255, 0), 2)
    image_tree = cv2.drawContours(img.copy(), contours_tree, -1, (0, 255, 0), 2)    
    cv2.imshow('original', img)
    cv2.imshow('canny', canny)
    cv2.imshow('contours_external', image_external)
    cv2.imshow('contours_tree', image_tree)
    
cv2.destroyAllWindows()