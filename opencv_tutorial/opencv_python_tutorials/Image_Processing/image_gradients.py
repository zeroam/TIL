# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:30:15 2019

@author: jone
"""

import cv2
from matplotlib import pyplot as plt

img_origin = cv2.imread('img/sudoku.png')
img = cv2.cvtColor(img_origin, cv2.COLOR_RGB2BGR)
canny = cv2.Canny(img, 30, 70)

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y', 'Canny']

# plt 사이즈 조정
plt.figure(figsize=(8, 6))

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
#%%
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/chessboard.jpg', 0)


# 사이즈 조정
h, w = img.shape[:2]
r = 400/w
dim = (int(r*w), int(r*h))
img = cv2.resize(img, dim)

canny = cv2.Canny(img, 30, 70)

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y', 'Canny']

for i in range(len(images)):
    cv2.imshow(titles[i], images[i])
    
cv2.waitKey(0)
cv2.destroyAllWindows()