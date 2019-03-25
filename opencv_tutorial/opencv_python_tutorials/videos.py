# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:09:09 2019

@author: jone
"""
#%%
import cv2

# cap.isOpened() - cap이 정상적으로 open 되었는지 확인
# False 값이면 open되지 않은 것
cap = cv2.VideoCapture(0)

# cap.get(prodId) / cap.set(prodId, value)를 통해 속성 변경 가능
# prodId - 3 : width, 4 : height
cap.set(3, 320)
cap.set(4, 240)

while(True):
    # ret : frame capture 한 결과(boolean)
    # frame : Capture한 frame
    ret, frame = cap.read()
    
    # 프레임에 대한 연산
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 연산된 프레임 보이기
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#%%
import cv2
from os import path

cap = cv2.VideoCapture(path.join('Dataset', 'y2mate_360p.mp4'))

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

#%%
import cv2
from os import path

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(path.join('Output', 'output.avi'), fourcc, 25.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # 이미지 반전, 0 : 상하, 1 : 좌우
        frame = cv2.flip(frame, 0)
        
        out.write(frame)
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()