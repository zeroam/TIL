## 참조링크

- [한글 번역본](<https://opencv-python.readthedocs.io/en/latest/doc/06.operation/operation.html>)
- [영문 원본](<https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html>)



## 튜토리얼

### Basic Operation(Basic Operations on Images)

- basic_operation.py

- 목표
  - 픽셀 값에 접근하고 수정할 수 있다.
  - 이미지의 기본 속성을 확인할 수 있다.
  - 이미지의 ROI(Region of Image)를 설정할 수 있다.
  - 이미지를 분리하고 합칠 수 있다.

- 픽셀에 접근하고 수정하기(Accessing and Modifying pixel values)

  ```bash
  # 이미지 로드하기
  >>> import cv2
  >>> import numpy as np
  >>> img = cv2.imread('lena.jpg')
  
  # 특정 pixel 값에 접근
  >>> px = img[100,200]
  >>> print(px)
  [157 100 190]
  
  # blue pixel만 접근
  >>> b = img[100,200,0]
  >>> print(b)
  157
  
  # 특정 pixel 값 수정
  >>> img[100,100] = [255,255,255]
  >>> print(img[100,100])
  [255 255 255]
  
  # numpy를 이용한 접근과 수정 - b,g,r 중 하나의 값만 접근가능
  >>> img.item(10,10,2) # Red값
  59
  >>> img.itemset((10,10,2), 100) #Red값을 100으로 변경
  >>> img.item(10,10,2)
  100
  ```

- 이미지 속성에 접근하기(Accessing Image Properties)

  - `img.shape`
    - tuple 형태로(형,렬, channel) 정보를 리턴함
  - `img.size`
    - 전체 pixel수 확인
  - img.dtype
    - 이미지의 Datatype 확인

  ```bash
  # 이미지 속성 접근하기
  >>> print(img.shape)
  (342, 548, 3)
  
  >>> print(img.size)
  562248
  
  >>> print(img.dtype)
  uint8
  ```

- 이미지 ROI(Image ROI)

  - 이미지 작업시에는 특정 pixel 단위보다는 특정 영역단위로 작업을 하게됨
  - 이것을 Region of Image(ROI)라고 함
  - ROI 설정은 Numpy의 indexing 방법을 사용함

  ```python
  import cv2
  
  img = cv2.imread('baseball-player.jpg')
  cv2.imshow('img', img)
  cv2.waitKey(0)
  
  # img[행의 시작점: 행의 끝점, 열의 시작점: 열의 끝점]
  ball = img[435:480, 817:884]
  img[490:535, 817:884] = ball # 다른 영역에 paste
  cv2.imshow('img', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
  ```

- 이미지 Channel

  - Color Image는 3개의 B,G,R로 구성이 되어 있으며, 이것을 각 채널별로 분리할 수 있음
  - 개별적인 채널들은 다시 합쳐질 수도 있음

  ```bash
  # 채널 분리 및 합치기
  >>> b, g, r= cv2.split(img)
  >>> img = cv2.merge((r,g,b))
  
  # Numpy indexing 접근 방법으로 표현
  # cv2.split()은 비용이 많이 드는 함수이기 때문에
  # numpy indexing 방법을 사용하는 것이 효율적
  >>> b = img[:,:,0] # 0 : Blue, 1 : Green, 2 : Red
  >>> img[:,:,2] = 0 # Red Channel을 0으로 변경. Red 제거하는 효과.
  ```



- 이미지에 테두리 만들기(Making Borders for Images(Padding))
  - `cv2.copyMakeBorder(src, top, bottom, left, right, borderType)`
    - src - 이미지
    - top, bottom, left, right - 각 방향별 픽셀 두께
    - borderType - 테두리 타입
      - cv2.BORDER_CONSTANT
      - cv2.BORDER_REFLECT
      - cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT
      - cv2.BORDER_REPLICATE
      - cv2.BORDER_WRAP

![result](result.png)



### 이미지 연산



### 이미지 Processing



### 이미지 임계처리



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

