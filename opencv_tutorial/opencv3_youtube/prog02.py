# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:48:40 2019

@author: jone
"""

import cv2
import os.path

def main():
    img_path = os.path.join('Dataset', 'lena_color_512.tif')
    img = cv2.imread(img_path)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()