# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:32:46 2019

@author: jone
"""

#%% Moments
import cv2

img = cv2.imread('img/tetris_blocks.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 225, 255, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 첫번째 contours의 moment 특징 추출
cnt = contours[0]
M = cv2.moments(cnt)

# contours의 특징을 찾을 수 있는 기본 정보
print('contours 기본정보:', M.items())

# Contour Area : contour 면적
print('contour 면적:', cv2.contourArea(cnt))

# Contour Perimeter : contour의 둘레 길이
print('폐곡선 도형을 만들어 둘레 길이:', cv2.arcLength(cnt, True))
print('시작점, 끝점을 연결하지 않고 둘레 길이:', cv2.arcLength(cnt, False))

#%% Contour Approximation
import cv2
from matplotlib import pyplot as plt

img_origin = cv2.imread('img/hand.jpg')
img = cv2.cvtColor(img_origin, cv2.COLOR_BGR2RGB)
img1 = img.copy()
img2 = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 30, 150, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

# 적용하는 숫자가 커질 수록 Point의 갯수는 감소
epsilon1 = 0.01*cv2.arcLength(cnt, True)
epsilon2 = 0.1*cv2.arcLength(cnt, True)

approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
cv2.drawContours(img1, [approx1], 0, (0, 255, 0), 3)
cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3)

titles = ['Original', '1%', '10%']
images = [img, img1, img2]

for i in range(3):
    plt.subplot(1, 3, i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

#%% Contour Approximation2
import cv2

def nothing(x):
    pass

img_origin = cv2.imread('img/balloon.png')
img_gray = cv2.cvtColor(img_origin, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('canny')
cv2.createTrackbar('C', 'canny', 1, 255, nothing)
cv2.namedWindow('approximation')
cv2.createTrackbar('A', 'approximation', 0, 100, nothing)

while(1):
    if cv2.waitKey(1) & 0xff == 27:
        break
    c = cv2.getTrackbarPos('C', 'canny')
    canny = cv2.Canny(img_origin, c, 3*c)
    
    img = img_origin.copy()
    img1 = img_origin.copy()
    
    a = cv2.getTrackbarPos('A', 'approximation')
    image, contours, heirachy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    
    epilson = a*0.01*cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epilson, True)
    
    cv2.drawContours(img, [cnt] , 0, (0,255, 0), 3)
    cv2.drawContours(img1, [approx], 0, (0, 255, 0), 3)
    
    cv2.imshow('canny', canny)
    cv2.imshow('original', img)
    cv2.imshow('approximation', img1)
    
    
cv2.destroyAllWindows()

#%% Contours Hull
import cv2

def nothing(x):
    pass

img_origin = cv2.imread('img/balloon.png')
canny = cv2.Canny(img_origin, 30, 90)

while(1):
    if cv2.waitKey(1) & 0xff == 27:
        break
    
    img = img_origin.copy()
    img1 = img_origin.copy()
    
    image, contours, heirachy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    
    
    hull = cv2.convexHull(cnt)
    
    cv2.drawContours(img, [cnt] , 0, (0,255, 0), 3)
    cv2.drawContours(img1, [hull], 0, (0, 255, 0), 3)
    
    cv2.imshow('original', img)
    cv2.imshow('convex hull', img1)
  
# Checking Convexity
print(cv2.isContourConvex(cnt)) # 풍선 모양 : False
print(cv2.isContourConvex(hull)) # 외곽선 : True
    
cv2.destroyAllWindows()

#%% Drawing Contours
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/lightning.png')
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

# Straight Rectangle
x, y, w, h = cv2.boundingRect(cnt)
img1 = cv2.rectangle(img1, (x,y), (x+w, y+h), (0, 255, 0), 3)   # green

# Rotated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img1 = cv2.drawContours(img1, [box], 0, (0, 0, 255), 3)         # blue

# Minimum Enclosing Circle
(x,y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img1 = cv2.circle(img1, center, radius, (255, 255, 0), 3)       # yellow

# Fitting an Ellipse
ellipse = cv2.fitEllipse(cnt)
img1 = cv2.ellipse(img1, ellipse, (255, 0, 0), 3)               # Red

titles = ['Original', 'Result']
images = [img, img1]

plt.figure(figsize=(8, 4))

for i in range(2):
    plt.subplot(1, 2, i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()