# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 19:51:14 2019

@author: imdff
"""

#%% Scaling
import cv2

img = cv2.imread('img/logo.png')

# 행 : Height, 열 : Width
height, width = img.shape[:2]

# 이미지 축소
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Manual Size 지정
zoom1 = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

# 배수 Size 지정
zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Original', img)
cv2.imshow('Shrink', shrink)
cv2.imshow('Zoom1', zoom1)
cv2.imshow('Zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Translation
import cv2
import numpy as np

img = cv2.imread('img/logo.png')

rows, cols = img.shape[:2]

# 변환 행렬, x축으로 10, Y축으로 20 이동
M = np.float32([[1, 0, 10], [0, 1, 20]])

dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Original', img)
cv2.imshow('Translation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Rotation
import cv2

img = cv2.imread('img/logo.png')

rows, cols = img.shape[:2]

# 이미지의 중심점을 기준으로 90도 회전하면서 0.5배 Scale
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.5)

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Rotations', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Affine Transformation
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/chessboard.jpg')

# RGB -> BGR로 변환
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

rows, cols, ch = img.shape

pts1 = np.float32([[200, 100], [400, 100], [200, 200]])
pts2 = np.float32([[200, 300], [400, 200], [200, 400]])

# pts1의 좌표에 표시. Affine 변환 후 이동 점 확인
cv2.circle(img, (200, 100), 10, (255, 0, 0), -1)
cv2.circle(img, (400, 100), 10, (0, 255, 0), -1)
cv2.circle(img, (200, 200), 10, (0, 0, 255), -1)

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('image')
plt.subplot(122), plt.imshow(dst), plt.title('Affine')
plt.show()

#%% Perspective Transformation
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_origin = cv2.imread('img/perspective.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# [x, y] 좌표점을 4x2의 행렬로 작성
# 좌표점은 좌상 -> 좌하 -> 우상 -> 우하
pts1 = np.float32([[414, 393], [75, 745], [489, 393], [245, 745]])

# 좌표의 이동점
pts2 = np.float32([[100, 100], [100, 800], [800, 100], [800, 800]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인
cv2.circle(img, (414, 393), 20, (255,0,0), -1)
cv2.circle(img, (75, 745), 20, (0,255,0), -1)
cv2.circle(img, (489, 393), 20, (0,0,255), -1)
cv2.circle(img, (245, 745), 20, (0,0,0), -1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (1500, 1000))

plt.subplot(121), plt.imshow(img), plt.title('image')
plt.subplot(122), plt.imshow(dst), plt.title('Perspective')
plt.show()
