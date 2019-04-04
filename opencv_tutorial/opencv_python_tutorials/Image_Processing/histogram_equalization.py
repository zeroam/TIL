# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:35:07 2019

@author: jone
"""

#%% Histogram Equalization
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/bld1.jpg')

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()

# cdf의 값이 0인 경우는 mask처리를 하여 계산에서 제외
# mask 처리가 되면 Numpy 계산에서 제외됨
# 아래는 cdf array에서 값이 0인 부분을 mask처리함
cdf_m = np.ma.masked_equal(cdf, 0)

# Histogram Equalization 공식
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())

# Mask 처리를 했던 부분을 다시 0으로 변환
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

img2 = cdf[img]

plt.figure(figsize=(8,6))
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(img2), plt.title('Equalization')
plt.show()

#%% OpenCV function
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/bld1.jpg', 0)

# OpenCV의 Equalization 함수
img2 = cv2.equalizeHist(img)

dst = np.hstack((img, img2))
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()