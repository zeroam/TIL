## 참조링크
- 유튜브 : https://www.youtube.com/playlist?list=PLiHa1s-EL3vjr0Z02ihr6Lcu4Q0rnRvjm

- 이미지 데이터 셋
  - [UCI(Machine Learning Repository)](https://archive.ics.uci.edu/ml/datasets.html)
  - [ImageProcessingPlace.com](<http://www.imageprocessingplace.com/root_files_V3/image_databases.htm>)
  - [USC-SIPI Image Database](<http://sipi.usc.edu/database/>)



## 튜토리얼

- prog08.py
  - image = set of numbers
  - image type -> numpy.ndarray(N dimensional arrays)
  - image data type -> uint8(Unsigned Integer 8-bits)
    - 00000000 = 0x00 = 0
    - 11111111 = 0xFF = 255
    - 1 픽셀이 나타낼 수 있는 색 -> 256 x 256 x 256
  - [125 137 226] = Blue Green Red(channel)
  - gray-scale 이미지는 color 이미지 크기의 1/3
    - 0 : black, 255 : white

```python
print(type(img1)) # 이미지 타입 -> numpy.ndarray(N dimensional arrays)

print(img1.dtype) # 데이터 타입 -> uint8(Unsigned Integer 8-bits)
print(img1.shape) # 모양 (너비, 높이, 깊이)
print(img1.ndim) # 차원(깊이)
print(img1.size) # 이미지 사이즈
```



- prog09.py

```python
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
```



- prog10.py
  - OpenCV BGR Palette with Trackbars

```python
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
```

