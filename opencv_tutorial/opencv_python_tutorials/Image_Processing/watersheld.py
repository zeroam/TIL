# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:26:19 2019

@author: jone
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/coin.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# binary 이미지로 변환(grayscale로 변환)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Morphology의 opening, closing을 이용하여 이미지의 노이즈나 hole을 제거
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# dilate를 통해서 확실한 Background
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# distance transform을 적용하면 중심으로부터 Skeleton Image를 얻을 수 있음
# 즉, 중심으로부터 점점 옆어져 가는 영상
# 그 결과에서 thresh를 이용하여 확실한 FG를 파악
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.5*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

# Background에서 Foreground를 제외한 영역을 Unknown 영역으로 파악
unknown = cv2.subtract(sure_bg, sure_fg)

# FG에 Labelling 작업
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# watershed를 적용하고 경계 영역에 색지정
markers = cv2.watershed(img, markers)

img[markers == -1] = [255, 0, 0]

images = [gray,thresh,sure_bg,  dist_transform, sure_fg, unknown, markers, img]
titles = ['Gray','Binary','Sure BG','Distance','Sure FG','Unknow','Markers','Result']

plt.figure(figsize=(12, 8))
for i in range(len(images)):
    plt.subplot(2,4,i+1),plt.imshow(images[i]),plt.title(titles[i]),plt.xticks([]),plt.yticks([])
plt.show()