# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:02:33 2019

@author: jone
"""

import cv2
import numpy as np

img = cv2.imread('img/logo.png')
img = cv2.medianBlur(img, 5)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=25, minRadius=0, maxRadius=0)
circles = np.uint(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    
cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
