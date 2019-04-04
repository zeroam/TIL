# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:45:26 2019

@author: jone
"""
#%% Template Matching in OpenCV
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/messi.jpg', 0)
img2 = img.copy()
template = cv2.imread('img/messi_face.jpg', 0)
w, h = template.shape[::1]

# All the 6 methods for comparision in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMAL, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    
    plt.figure(figsize=(8,6))
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.axis('off')
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.axis('off')
    plt.suptitle(meth)
    
    plt.show()

#%% Template Matching with Multiple Objects
import cv2
import numpy as np

img_rgb = cv2.imread('img/matching.jpg')
img_copy = img_rgb.copy()
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('img/matching_template.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_copy, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
img = np.hstack((img_rgb, img_copy))
img = cv2.resize(img, (1600, 800))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()