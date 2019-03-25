# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:17:16 2019

@author: jone
"""

import cv2
import os.path

def main():
    img_path = os.path.join('Dataset', 'lena_color_512.tif')
    # 1 : default, 0 : gray-scale
    img = cv2.imread(img_path, 0)
    
    output_path = os.path.join('Output', 'lena_color_512.jpg')
    
    cv2.imshow('Lena', img)
    cv2.imwrite(output_path, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
if __name__ == "__main__":
    main()