# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:42:01 2019

@author: jone
"""

import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    
    img1 = np.zeros((512, 512, 3), np.uint8)
    windowName = 'OpenCV BGR Color Palette'
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('B', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('G', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('R', windowName, 0, 255, emptyFunction)
    
    while(True):
        cv2.imshow(windowName, img1)
        
        # ESC 키 입력
        if cv2.waitKey(1) == 27:
            break
        
        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)
        
        img1[:] = [blue, green, red]
        
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()