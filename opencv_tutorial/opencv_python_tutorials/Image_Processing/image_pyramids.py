# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:39:33 2019

@author: jone
"""

#%% Gaussian Pyramids
import cv2

img = cv2.imread('img/monkey.tiff')

lower_reso = cv2.pyrDown(img)   # 원본 이미지의 1/4 사이즈
higher_reso = cv2.pyrUp(img)    # 원본 이미지의 4배 사이즈

cv2.imshow('img', img)
cv2.imshow('lower', lower_reso)
cv2.imshow('higher', higher_reso)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Laplacian Pyramids
import cv2

img = cv2.imread('img/monkey.tiff')
print(img.shape) # (512, 512, 3)

GAD = cv2.pyrDown(img)
print(GAD.shape) # (256, 256, 3)

GAU = cv2.pyrUp(GAD)
print(GAU.shape) # (512, 512, 3)

temp = cv2.resize(GAU, (512, 512))
res = cv2.subtract(img, temp)

cv2.imshow('res', res)
cv2.waitKey(0)
# 이미지 저장
cv2.imwrite('img/lap_pyramids.png', res)
cv2.destroyAllWindows()

#%%
import cv2
import numpy as np

STEP = 6

# 1단계
A = cv2.imread('img/apple.jpg')
B = cv2.imread('img/orange.jpg')


# 2단계
# A 이미지에 대한 Gaussian Pyramid를 생성
# 점점 작아지는 Pyramid
G = A.copy()
gpA = [G]
for i in range(STEP):
    G = cv2.pyrDown(G)
    gpA.append(G)
    
# B 이미지에 대한 Gaussian Pyramid 생성
# 점점 작아지는 Pyramid
G = B.copy()
gpB = [G]
for i in range(STEP):
    G = cv2.pyrDown(G)
    gpB.append(G)
    
    
# 3단계
# A 이미지에 대한 Laplacian Pyramid 생성
lpA = [gpA[STEP-1]]  # n번쨰 추가된 Gaussian Image
for i in range(STEP-1, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)
    
# B 이미지에 대한 Laplacian Pyramid 생성
lpB = [gpB[STEP-1]]
for i in range(STEP-1, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)
   
    
# 4단계
# Laplacian Pyramid를 누적으로 좌측과 우측으로 재결합
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))
    LS.append(ls)
    
    
# 5단계
ls_ = LS[0] # 좌측과 우측이 합쳐진 가장 작은 이미지
for i in range(1, STEP):
     ls_ = cv2.pyrUp(ls_)    # Up scale
     ls_ = cv2.add(ls_, LS[i]) # Up Scale된 이미지에 외곽서늘 추가하여 선명한 이미지로 생성
    
# 원본 이미지를 그대로 붙인 경우
real = np.hstack((A[:, :int(cols/2)], B[:, int(cols/2):]))

cv2.imshow('real', real)
cv2.imshow('blending', ls_)
cv2.waitKey(0)
cv2.destroyAllWindows()
