# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:52:34 2019

@author: jone
"""
#%%
import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('img/chessboard2.jpg')
img = cv2.resize(img, (800, 800))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.namedWindow('image')
cv2.createTrackbar('threshold', 'image', 200, 400, nothing)
cv2.namedWindow('canny')
cv2.createTrackbar('canny', 'canny', 50, 255, nothing)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    img_copy = img.copy()
    threshold = cv2.getTrackbarPos('threshold', 'image')
    c = cv2.getTrackbarPos('canny', 'canny')
    if threshold < 50:
        threshold = 50

    edges = cv2.Canny(gray, c, 3*c, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold)
    
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
        
        cv2.line(img_copy, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    cv2.imshow('canny', edges)
    cv2.imshow('image', img_copy)

cv2.destroyAllWindows()

#%% 확률 허프 변환
import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('img/building.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 50, 150, apertureSize=3)

cv2.namedWindow('image')
cv2.createTrackbar('threshold', 'image', 100, 255, nothing)
cv2.createTrackbar('min_length', 'image', 100, 500, nothing)
cv2.createTrackbar('max_gap', 'image', 0, 100, nothing)

while(1):
    if cv2.waitKey(1) & 0xFF == 27:
        break
    img_copy = img.copy()
    threshold = cv2.getTrackbarPos('threshold', 'image')
    min_length = cv2.getTrackbarPos('min_length', 'image')
    max_gap = cv2.getTrackbarPos('max_gap', 'image')
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold, min_length, max_gap)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img_copy, (x1,y1), (x2,y2), (0,255,0), 2)
            
    cv2.imshow('image', img_copy)
    
cv2.destroyAllWindows()