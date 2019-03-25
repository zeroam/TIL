# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:34:40 2019

@author: jone
"""

import cv2
import os.path

def main():
    img_path = os.path.join('Dataset', 'lena_color_512.tif')
    img1 = cv2.imread(img_path, 1)
    
    print(type(img1))
    
    print(img1.dtype)
    print(img1.shape)
    print(img1.ndim)
    print(img1.size)
    
    cv2.imshow('Lena', img1)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
if __name__ == "__main__":
    main()