# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:18:41 2019

@author: jone
"""
#%%
import cv2
from os import path

fname = path.join('Dataset', 'lena.jpg')

original = cv2.imread(fname, cv2.IMREAD_COLOR)
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Original', cv2.WINDOW_AUTOSIZE)

cv2.imshow('Original', original)
cv2.imshow('Gray', gray)
cv2.imshow('Unchange', unchange)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
import cv2
from os import path

fname = path.join('Dataset', 'lena.jpg')
img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:  # esc key
    cv2.destroyAllWindows()
elif k == ord('s'): # 's' key
    cv2.imwrite(path.join('Output', 'lenagray.png'), img)
    cv2.destroyAllWindows()
    
#%%
import cv2
from matplotlib import pyplot as plt
from os import path

img = cv2.imread(path.join('Dataset', 'lena.jpg'), 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([]) # X축, Y축의 값을 숨김
plt.show()

#%%
import cv2
from matplotlib import pyplot as plt
from os import path

img = cv2.imread(path.join('Dataset', 'lena.jpg'), cv2.IMREAD_COLOR)


#b, g, r = cv2.split(img)   # img파일을 b,g,r로 분리
#img2 = cv2.merge([r,g,b]) # b, r을 바꿔서 Merge
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR이미지를 RGB이미지로 바꾸기
plt.imshow(img2)
plt.xticks([]), plt.yticks([]) # X축, Y축의 값을 숨김
plt.show()