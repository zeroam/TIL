# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:14:05 2019

@author: jone
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

train_data = np.random.randint(0, 100, (25,2)).astype(np.float32)
response = np.random.randint(0, 2, (25, 1)).astype(np.float32)

red = train_data[response.ravel() == 0] # red는 0 class로 분류
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')

blue = train_data[response.ravel() == 1] # blue는 1 class로 분류
plt.scatter(blue[:,0], blue[:,1], 80, 'b', 's')

newcomer = np.random.randint(0, 100, (1,2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, response)
ret, results, neighbours, dist = knn.findNearest(newcomer, 3) # k값을 3으로 설정

print('result: ', results)
print('neighbours :', neighbours)
print('distance :', dist)

plt.show()
