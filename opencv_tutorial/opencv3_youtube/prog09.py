# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:02:19 2019

@author: jone
"""

import cv2
import numpy as np

def main():
    # 0 : 검은색 이미지(512 x 512)
    img1 = np.zeros((512, 512, 3), np.uint8)
    
    # 원그리기
    # params : 원본, 점1, 점2, 선색, 두께
    cv2.line(img1, (0, 99), (99, 0), (255, 0, 0), 2)
    
    # 사각형
    # params : 원본, 점1, 점2, 선색, 두께
    cv2.rectangle(img1, (40, 60), (80, 70), (0, 255, 0), 2)
    
    # 원
    # params : 원본, 중심, 반지름, 선색, 두께
    cv2.circle(img1, (60, 60), 10, (0, 0, 255), 5)
    
    # 타원형
    # params : 원본, 중심, 축(너비, 높이), 원 각도, 시작 각, 끝 각, 선색, 두께
    cv2.ellipse(img1, (160, 260), (30, 70), 30, 0, 360, (127, 127, 127), -1)
    
    # 다각형
    points = np.array([[80, 2], [125, 0], [179, 0], [230, 5], [30, 50]], np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(img1, [points], True, (0, 255, 255))
    
    # 텍스트
    # params : 원본, 텍스트, 시작점, 폰트, 폰트 크기, 글색, (두께)
    text1 = 'Test Text'
    cv2.putText(img1, text1, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
    cv2.imshow('Lena', img1)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
if __name__ == "__main__":
    main()