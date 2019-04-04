# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:31:42 2019

@author: jone
"""
#%% Fourier Transform in Numpy
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/messi.jpg', 0)
f = np.fft.fft2(img)
# 좌상단에 있는 저주파 영역을 중앙으로 옮김
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.figure(figsize=(8,6))
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

"""
주파수로 연산하기
"""
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)   # 이미지의 중심 좌표

d = 30
fshift[crow-d:crow+d, ccol-d:ccol+d] = 0

# 푸리에 변환결과를 다시 이미지로 변환
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.figure(figsize=(12, 6))
plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Input Image'), plt.axis('off')
plt.subplot(132), plt.imshow(img_back, cmap='gray'), plt.title('Image after HPF'), plt.axis('off')
plt.subplot(133), plt.imshow(img_back), plt.title('Result in JET'), plt.axis('off')

plt.show()

#%% Fourier Transform in OpenCV
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/messi.jpg', 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))

plt.figure(figsize=(8,6))
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Input Image'), plt.axis('off')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray'), plt.title('Magnitude Spectrum'), plt.axis('off')
plt.show()

"""
고주파 영역 제거 -> blur 효과
"""
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)

# create a mask first, center square is 1, remaining all zeros
# 아래는 d 사이즈의 사각형을 생성한 후, 사각형 바깥을 제거하는 형태
# 즉, 고주파 영역을 제거하게 됨
# d 값이 작을수록 사각형이 작고, 바깥영역(고주파 영역)이 많이 제거되기 때문에 이미지가 뭉개지고
# d 값이 클수록 사각형이 크고, 바깥영역(고주파 영역)이 적게 제거되기 떄문에 원래 이미지와 가까워
d = 30
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-d:crow+d, ccol-d:ccol+d] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])

plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Input Image'), plt.axis('off')
plt.subplot(122), plt.imshow(img_back, cmap='gray'), plt.title('Magnitude Spectrum'), plt.axis('off')
plt.show()