## 참조링크

- [한글 번역본](<https://opencv-python.readthedocs.io/en/latest/doc/08.imageProcessing/imageProcessing.html>)
- [영문 원본](<https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html>)



## 튜토리얼

### 이미지 Processing

- image_processing.py

- 목표
  - 디지털 영상의 표현 방법에 대해서 알 수 있다.
  - Color-space 중 Binary Image, Grayscale, RGB, HSV에 대해서 알 수 있다.
  - 각 Color-space 변환 방법에 대해서 알 수 있다.
  - 동영상에서 간단한 Object Tracking을 할 수 있다.
  - cv2.cvtColor(), cv2.inRange() 함수에 대해서 알 수 있다.
- Digital Image
  - 디티절 영상은 2차원 행렬의 형태로 표현이 됨
  - 각 격자가 하나의 pixel이 되고 이를 bitmap image라고 함
  - 각 pixel의 위치는 2가지 형태로 표현을 할 수가 있는데, 영상좌표와 행렬 위치로 표현이 됨
    - 영상 좌표 -> (x, y)
    - 행렬 위치 -> (r, c)
- Digital Image의 유형
  - Binary Image
    - pixel당 1bit로 표현하는 영상
    - 흰색과 검은색으로만 표현이 되는 영상
    - dithering : binary image의 밀도를 조절하여 밝기를 표현하는 방법
- Grayscale Image
  - pixel당 8bit, 즉 256단계의 명암(빛의 세기)를 표현할 수 있는 이미지
- Color Image
  - pixel의 색을 표현하기 위해 pixel당 24bit를 사용함(총 16,777,216 색)
  - pixel은 RGB 각각을 위해서 8bit를 사용하게 됨
  - 각 pixel당 3byte를 사용하기 때문에 용량이 큼
    - 이를 해결하기 위해 lookup table을 사용하여, 해당 pixel에는 index만을 저장하기도 함
- RGB Color-space
  - 빛의 삼원색인 빨간색, 초록색, 파란색을 기본 색으로 사용을 함
  - 정육면체 모델 형태로 표현할 수 있음
- HSV Color-space
  - 이미지 처리에서 가장 많이 사용되는 형태의 Color 모델
  - 하나의 모델에서 색과 채도, 명도를 모두 알 수 있음
    - H(ue) : 색상. 일반적인 색을 의미함. 원추모형에서 각도로 표현이 됨.
    - S(aturation) : 채도. 색의 순수성을 의미하며 일반적으로 짙다, 흐리다로 표현이 됨. 중심에서 바깥쪽으로 이동하면 채도가 높음.
    - V(alue) : 명도. 색의 밝고 어두운 정도. 수직축의 깊으로 표현. 어둡다 밝다로 표현이 됨.

- Color-space 변환

  - `cv2.cvtColor(src, code)`

    - src - image
    - code - 변환 코드

  - 목록 확인

    ```python
    >>> import cv2
    >>> flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    >>> print(flags)
    ```

  - BGR -> Grayscale로 변환 : cv2.COLOR_BGR2GRAY

  - BGR -> HSV로 변환 : cv2.COLOR_BGR2HSV

- Object Tracking

  - 영상에서 파란색 부분을 찾아서 binary image로 보여줌
  - 절차
    - Video로부터 Frame을 읽어 들임
    - frame을 HSV로 변환
    - 변환한 이미지에서 blue 영역을 찾아서 mask를 생성
    - frame에 mask를 적용하여 이미지를 보여줌

  ```python
  
  import cv2
  import numpy as np
  
  # Camera 객체를 생성 후 사이즈로 320 x 240으로 조정
  cap = cv2.VideoCapture(0)
  cap.set(3, 320)
  cap.set(4, 240)
  
  while(1):
      # camera에서 frame capture
      ret, frame = cap.read()
      
      if ret:
          # BGR -> HSV로 변환
          hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
          
          # blue 영역의 from ~ to
          lower_blue = np.array([110, 50, 50])
          upper_blue = np.array([130, 255, 255])
          
          # 이미지에서 blue 영역
          mask = cv2.inRange(hsv, lower_blue, upper_blue)
          
          # bit 연산자를 통해서 blue 영역만 남김
          res = cv2.bitwise_and(frame, frame, mask=mask)
          
          cv2.imshow('frame', frame)
          cv2.imshow('mask', mask)
          cv2.imshow('res', res)
          
      if cv2.waitKey(1) & 0xFF == 27:
          break
      
  cap.release()
  cv2.destroyAllWindows()
  ```





### 이미지 임계처리

- 목표

  - 이미지 이진화의 방법인 Simple thresholding, Adaptive thresholding, Otsu's thresholding에 대해서 알 수 있다.
  - cv2.threshold(), cv2.adaptiveThreshold() 함수에 대해서 알 수 있다.

- 기본 임계처리

  - 이진화 : 영상을 흑/백으로 분류하여 처리하는 것
  - 이진화를 할 때 기준이되는 임계값을 어떻게 결정할 것인지가 중요한 문제가 됨
    - 임계값보다 크면 백, 작으면 흑
  - 기본 임계처리는 사용자가 고정된 임계값을 결정하고 그 결과를 보여주는 단순한 형태
  - `cv2.threshold(src, thresh, maxval, type) -> retval, dst`
    - src - image : single-channel 이미지(grayscale 이미지)
    - thresh - 임계값
    - maxval - 임계값을 넘었을 때 적용할 value
    - type - thresholding type
      - cv2.THRESH_BINARY
      - cv2.THRESH_BINARY_INV
      - cv2.THRESH_TRUNC
      - cv2.THRESH_TOZERO
      - cv2.THRESH_TOZERO_INV

  ![squirrel_result](img/squirrel_result.png)

  - 예제

  ```python
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  
  img = cv2.imread('img/squirrel.jpg', 0)
  
  # 사이즈 조정
  h, w = img.shape
  r = 300/w
  dim = (int(r*w), int(r*h))
  img_resize = cv2.resize(img, dim)
  
  cv2.imshow('img', img_resize)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
  
  ret, thresh1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
  ret, thresh2 = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)
  ret, thresh3 = cv2.threshold(img,127,255, cv2.THRESH_TRUNC)
  ret, thresh4 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO)
  ret, thresh5 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO_INV)
  
  titles =['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
  images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
  
  for i in range(6):
      plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
      plt.title(titles[i])
      plt.xticks([]),plt.yticks([])
      
  plt.show()
  
  ```



- 적응 임계처리

  - 기본 임계처리의 경우 임계값을 이미지 전체에 적용하여 처리하기 때문에 이미지에 음영이 다르면 일부 영역이 모두 흰색 또는 검정색으로 보여지게 됨
  - 이런 문제를 해결하기 위해 이미지의 작은 영역별로 thresholding을 함
    - cv2.adaptiveThreshold() 함수 사용
  - `cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)`
    - src - grayscale image
    - maxValue - 임계값
    - adaptiveMethod - thresholding value를 결정하는 계산 방법
      - cv2.ADAPTIVE_THRESH_MEAN_C : 주변영역의 평균값으로 결정
      - cv2.ADAPTIVE_THRESH_GAUSSIAN_C :
    - thresholdType - thresholding을 적용할 영역 사이즈
    - C - 평균이나 가중평균에서 차감할 값

  ```python
  import cv2
  from matplotlib import pyplot as plt
  
  img = cv2.imread('img/squirrel.jpg', 0)
  # img = cv2.medianBlur(img, 5)
  
  ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
  th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
  th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
  
  titles = ['Original', 'Global', 'Mean', 'Gaussian']
  
  images = [img, th1, th2, th3]
  
  for i in range(4):
      plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
      plt.title(titles[i])
      plt.xticks([]), plt.yticks([])
      
  plt.show()
  ```

  

![squirrel_adaptive](img/squirrel_adaptive.png)





### 이미지의 기하학적 변형



### Image Smoothing



### Morphological Transformations



### Image Gradients



### Image Pyramids



### Image Contours



### Contour Feature



### Contour Property



### Contours Hierarchy



### 히스토그램



### 히스토그램 균일화



### 2D Histogram



### 푸리에 변환



### 템플릿 매칭



### 허프 변환

