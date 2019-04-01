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

-  image_transformations.py

- 목표

  - 기하학적 변형에 대해서 알 수 있다.
  - cv2.getPerspectiveTransform() 함수에 대해서 알 수 있다.

- Transformations(변환)

  - 변환이란 수학적으로 표현하면 다음과 같다

    -> 좌표 x를 좌표 x'로 변환하는 함수

  - 예로는 사이즈 변경(Scaling), 위치변경(Translation), 회전(Rotation) 등이 있다

- 변환의 종류

  - 강체변환(Ridid-Body) : 크기 및 각도가 보존(ex; Translation, Rotation)
  - 유사변환(Similarity) : 크기는 변하고 각도는 보존(ex; Scaling)
  - 선형변환(Linear) : Vector 공간에서의 이동. 이동변환은 제외
  - Affine : 선형변환과 이동변환까지 포함. 선의 수평선은 유지(ex; 사각형 -> 평행사변형)
  - Perspective : Affine 변환에 수평성도 유지되지 않음. 원근변환

- **Scaling**

  - Scaling은 이미지의 사이즈가 변하는 것
  - OpenCV에서는 cv2.resize() 함수를 사용하여 적용할 수 있음
  - 사이즈가 변하면 pixel 사이의 값을 결정해야 하는데, 이 때 사용하는 것을 보간법(Interpolation method)라고 함
    - 사이즈를 줄일 때 : cv2.INTER_AREA
    - 사이즈를 크게 할 때 : cv2.INTER_CUBIC, cv2.INTER_LINEAR
  - `cv2.resize(img, dsize, fx, fy, interpolation)`
    - img - image
    - dsize - Manual Size, 가로, 세로 형태의 tuple(ex; (100,200))
    - fx - 가로 사이즈의 배수. 2배로 크게하려면 2, 반으로 줄이려면 0.5
    - fy - 세로 사이즈의 배수
    - interpolation - 보간법

  ```python
  import cv2
  
  img = cv2.imread('img/logo.png')
  
  # 행 : Height, 열 : Width
  height, width = img.shape[:2]
  
  # 이미지 축소
  shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
  
  # Manual Size 지정
  zoom1 = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)
  
  # 배수 Size 지정
  zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
  
  cv2.imshow('Original', img)
  cv2.imshow('Shrink', shrink)
  cv2.imshow('Zoom1', zoom1)
  cv2.imshow('Zoom2', zoom2)
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  

- **Translation**

  - 이미지의 위치를 변경하는 변환
  - `cv2.warpAffine(src, M, dsize)`
    - src - Image
    - M - 변환 행렬
    - dsize(tuple) - ouput image size(ex; (width=colums, height=rows))

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread('img/logo.png')
  
  rows, cols = img.shape[:2]
  
  # 변환 행렬, x축으로 10, Y축으로 20 이동
  M = np.float32([[1, 0, 10], [0, 1, 20]])
  
  dst = cv2.warpAffine(img, M, (cols, rows))
  cv2.imshow('Original', img)
  cv2.imshow('Translation', dst)
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  

- **Rotation**

  - 물체를 평면상의 한 점을 중심으로 @만큼 회전하는 변환
  - 양의 각도는 시계반대 방향으로 회전을 함
  - 변환 행렬이 필요한데, 변환 행렬을 생성하는 함수가 cv2.getRotationMatrix2D()
  - `cv2.getRotationMatrix2D(center, angle, scale) -> M`
    - center - 이미지 중심 좌표
    - angle - 회전 각도
    - scale - scale factor

  ```python
  import cv2
  
  img = cv2.imread('img/logo.png')
  
  rows, cols = img.shape[:2]
  
  # 이미지의 중심점을 기준으로 90도 회전하면서 0.5배 Scale
  M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.5)
  
  dst = cv2.warpAffine(img, M, (cols, rows))
  
  cv2.imshow('Original', img)
  cv2.imshow('Rotations', dst)
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  

- Affine Transformation

  - 선의 평행선은 유지가 되면서 이미지를 변환하는 작업
  - 이동, 확대, Scale, 반전까지 포함된 변환
  - Affine 변환을 위해서는 3개의 Match가 되는 점이 있으면 변환행렬을 구할 수 있음

  ```python
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  
  img = cv2.imread('img/chessboard.jpg')
  
  # RGB -> BGR로 변환
  img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
  
  rows, cols, ch = img.shape
  
  pts1 = np.float32([[200, 100], [400, 100], [200, 200]])
  pts2 = np.float32([[200, 300], [400, 200], [200, 400]])
  
  # pts1의 좌표에 표시. Affine 변환 후 이동 점 확인
  cv2.circle(img, (200, 100), 10, (255, 0, 0), -1)
  cv2.circle(img, (400, 100), 10, (0, 255, 0), -1)
  cv2.circle(img, (200, 200), 10, (0, 0, 255), -1)
  
  M = cv2.getAffineTransform(pts1, pts2)
  
  dst = cv2.warpAffine(img, M, (cols, rows))
  
  plt.subplot(121), plt.imshow(img), plt.title('image')
  plt.subplot(122), plt.imshow(dst), plt.title('Affine')
  plt.show()
  ```

![affine_transform](img/affine_transform.png)



- **Perspective Tranformation**

  - Perspective(원근법) 변환
  - 직선의 성질만 유지되고, 선의 평행성은 유지가 되지 않는 변환
    - 기차길은 서로 평행하지만 원근변환을 거치면 평행성은 유지되지 못하고 하나의 점에서 만나는 것처럼 보임
  - 4개의 Point의 Input값과 이동할 Output Point가 필요
  - 변환 행렬을 구하기 위해서는 cv2.getPerspectiveTransform() 함수가 필요하며, cv2.warpPerspective() 함수에 변환행렬값을 적용하여 최종 결과 이미지를 얻을 수 있음

  ```python
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  
  img_origin = cv2.imread('img/perspective.jpg')
  img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
  
  # [x, y] 좌표점을 4x2의 행렬로 작성
  # 좌표점은 좌상 -> 좌하 -> 우상 -> 우하
  pts1 = np.float32([[414, 393], [75, 745], [489, 393], [245, 745]])
  
  # 좌표의 이동점
  pts2 = np.float32([[100, 100], [100, 800], [800, 100], [800, 800]])
  
  # pts1의 좌표에 표시. perspective 변환 후 이동 점 확인
  cv2.circle(img, (414, 393), 20, (255,0,0), -1)
  cv2.circle(img, (75, 745), 20, (0,255,0), -1)
  cv2.circle(img, (489, 393), 20, (0,0,255), -1)
  cv2.circle(img, (245, 745), 20, (0,0,0), -1)
  
  M = cv2.getPerspectiveTransform(pts1, pts2)
  
  dst = cv2.warpPerspective(img, M, (1500, 1000))
  
  plt.subplot(121), plt.imshow(img), plt.title('image')
  plt.subplot(122), plt.imshow(dst), plt.title('Perspective')
  plt.show()
  ```



### Image Smoothing

- image_smoothing.py

- 목표

  - 다양한 Filter를 이용하여 Blur 이미지를 만들 수 있다.
  - 사용자 정의 Filter를 적용할 수 있다.

- Image Filtering

  - 이미지도 음성 신호처럼 주파수로 표현할 수 있슴
    - 일반적으로 고주파는 밝기의 변화가 많은 곳, 즉 경계선 영역에서 나타나며, 일반적인 배경은 저주파로 나타남
    - 이것을 바탕으로 고주파를 제거하면 Blur 처리가 되며, 저주파를 제거하면 대상의 영역을 확인할 수 있음
  - Low-pass filter(LPF)와 High-pass filter(HPF)를 이용하며, LPF를 적용하면 노이즈 제거나 blur 처리를 할 수 있으며, HPF를 적용하면 경계선을 찾을 수 있음
  - OpenCV에서는 cv2.filter2D() 함수를 이용하며 이미지에 kernel(filter)를 적용하여 이미지를 Filtering 할 수 있음
  - Filter가 적용되는 방법
    - 이미지의 각 pixel에 kernel을 적용함
    - 5x5 kernel인 경우에 각 pixel에 5x5윈도우를 올려놓고, 그 영역안에 포함되는 값의 Sum을 한 후에 25로 나눔
    - 그 결과는 해당 윈도우 영역안의 평균값이 되고, 그 값을 해당 pixel에 적용하는 방식
  - kernel 사이즈를 조정하면서 결과를 확인할 수 있는 예제

  ```python
  import cv2
  import numpy as np
  
  def nothing(x):
      pass
  
  img = cv2.imread('img/squirrel.jpg')
  
  # 사이즈 조정
  h, w = img.shape[:2]
  r = 900/w
  dim = (int(r*w), int(r*h))
  img = cv2.resize(img, dim)
  
  cv2.namedWindow('image')
  cv2.createTrackbar('K', 'image', 1, 20, nothing)
  
  while(1):
      if cv2.waitKey(1) & 0xFF == 27:
          break
      k = cv2.getTrackbarPos('K', 'image')
      
      # (0, 0)이면 에러가 발생함으로 1로 치환
      if k == 0:
          k = 1
          
      # trackbar에 의해서 (1,1) ~ (20,20) kernel 생성
      kernel = np.ones((k,k), np.float32) / (k**2)
      dst = cv2.filter2D(img, -1, kernel)
      
      cv2.imshow('image', dst)
      
  cv2.destroyAllWindows()
  ```

  

- Image Blurring

  - Image Blurring은 low-pass filter를 이미지에 적용하여 얻을 수 있음
  - 고주파 영역을 제거함으로써 노이즈를 제거하거나 경계선을 흐리게 할 수 있음
  - **Averaging**
    - Box 형태의 kernel을 이미지에 적용한 후 평균값을 box의 중심점에 적용하는 형태
    - cv2.blur() 또는 cv2.boxFilter() 함수로 적용할 수 있음
    - `cv2.blur(src, ksize)`
      - src - channel 수는 상관 없으나, depth(Data Type)은 CV_8U, CV_16U, CV_16S, CV_32F or CV_64F
      - ksize - kernel 사이즈(ex; (3,3))
  - **Gaussian Filtering**
    - box filter는 동일한 값으로 구성된 kernel을 사용하지만, Gaussian Filter는 Gaussian 함수를 이용한 Kernel을 적용함
      - kernel 행렬의 값을 Gaussian 함수를 통해서 수학적으로 생성하여 적용
      - kernel의 사이즈는 양수이면서 홀수로 지정을 해야함
      - 이미지의 Gaussian Noise(전체적으로 밀도가 동일한 노이즈, 백색노이즈)를 제거하는데 가장 효과적
    - `cv2.GaussianBlur(img, ksize, sigmaX)`
      - img - channel 수는 상관 없으나, depth(Data Type)은 CV_8U, CV_16U, CV_16S, CV_32F or CV_64F
      - ksize - (width, height) 형태의 kernel size. width와 height은 서로 다를 수 있지만, 양수의 홀수로 지정해야 함
      - sigmaX - Gaussian kernel standard deviation in X direction
  - **Median Filtering**
    - kernel window와 pixel의 값들을 정렬한 후에 중간값을 선택하여 적용
      - salt-and-pepper noise 제거에 효과적
    - `cv2.medianBlur(src, ksize)`
      - src - 1,3,4 channel image. depth가 CV_8U, CV_16U, or CV_32F이면 ksize는 3또는 5, CV_8U이면 더 큰 ksize 가능
      - ksize - 1보다 큰 홀수
  - **Bilateral Filtering**
    - 지금까지의 Blur처리는 경계선까지 Blur 처리가되어 경계선이 흐려지게 됨
    - Bilateral Filtering(양방향 필터)은 경계선을 유지하면서 Gaussian Blur 처리를 해주는 방법
      - Gaussian 필터를 적용하고, 또 하나의 Gaussian 필터를 주변 pixel까지 고려하여 적용하는 방식
    - `cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)`
      - src - 8-bit, 1 or 3 Channel image
      - d - filtering시 고려할 주변 pixel 지름
      - sigmaColor - Color를 고려할 공간. 숫자가 크면 멀리 있는 색도 고려함
      - sigmaSpace - 숫자가 크면 멀리 있는 pixel도 고려함

  ```python
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  
  img = cv2.imread('img/squirrel.jpg')
  
  # pyplot을 사용하기 위해 BGR을 RGB로 변환
  b,g,r = cv2.split(img)
  img = cv2.merge([r,g,b])
  
  # 일반 Blur
  dst1 = cv2.blur(img, (7,7))
  
  # GaussianBlur
  dst2 = cv2.GaussianBlur(img, (5,5), 0)
  
  # Median Blur
  dst3 = cv2.medianBlur(img, 9)
  
  # Bilateral Filtering
  dst4 = cv2.bilateralFilter(img, 9, 75, 75)
  
  images = [img, dst1, dst2, dst3, dst4]
  titles = ['Original', 'Blur(7X7)', 'Gaussian Blur(5X5)', 'Median Blur', 'Bilateral']
  
  for i in range(5):
      plt.subplot(3, 2, i+1), plt.imshow(images[i]), plt.title(titles[i])
      plt.xticks([]), plt.yticks([])
      
  plt.show()
  ```

  

![blurring_result](img/blurring_result.png)



### Morphological Transformations(형태론적 변환)

- morphological_transformations.py

- 목표 
  - Morphological 방법인 Erosion, Dilation, Opening, Closing에 대해서 알 수 있다.
  - cv2.erod(), cv2.dilate(), cv2.morphologyEx() 함수에 대해서 알 수 있다.
- **Theory**
  - Morphological Transformation은 이미지를 Segmentation 하여 단순화, 제거, 보정을 통해서 형태를 파악하는 목적으로 사용이 됨
    - 일반적으로 binary나 grayscale image에 사용이 됨
    - 사용하는 방법으로는 Dilation(팽창), Erosion(침식) 그리고 2개를 조합한 Opening과 Closing이 있음
    - 2가지 Input 값(원본이미지, structuring element)
      - structuring element
        - 원본이미지에 적용되는 kernel, 중심을 원점으로 사용할 수도 있고, 원점을 변경할 수도 있음
        - 일반적으로 꽉찬 사각형, 타원형, 십자형을 많이 사용함
- **Erosion(침식)**
  - 각 Pixel에 structuring element를 적용하여 하나라도 0이 있으면, 대상 pixel을 제거하는 방법
  - **이 방법은 작은 Object를 제거하는 효과가 있음**
  - `cv2.erode(src, kernel, dst, anchor, iterations, borderType, borderValue)`
    - src - the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
    - kernel - structuring element. cv2.getStructuringElement() 함수로 만들 수 있음
    - anchor - structuring element의 중심. default (-1, -1)로 중심점
    - iterations - erosion 적용 반복 횟수

![morph_erode](img/morph_erode.png)

- **Dilation(팽창)**
  - Erosion과 반대로 확장한 후 작은 구멍을 채우는 방법
  - Erosion과 마찬가지로 각 pixel에 structuring element를 적용함
    - 대상 pixel에 대해서 OR 연산을 수행함
    - 겹치는 부분이 하나라도 있으면 이미지를 확장함
  - **경계가 부드러워지고 구멍이 메꿔지는 효과**
  - `cv2.dilation(src, kernel, dst, anchor, iterations, borderType, borderValue)`
    - src – the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
    - kernel – structuring element. `cv2.getStructuringElemet()` 함수로 만들 수 있음.
    - anchor – structuring element의 중심. default (-1,-1)로 중심점.
    - iterations – dilation 적용 반복 횟수

![morph_dilate](img/morph_dilate.png)



- **Opening & Closing**

  - Opening과 Closing은 Erosion과 Dilation의 조합 결과

    - 차이점은 어느 것을 먼저 적용하는지

  - Opening

    - Erosion 적용 후 Dilation 적용
    - 작은 Object나 돌기 제거에 적합

  - Closing

    - Dilation 적용 후 Erosion 적용
    - 전체적인 윤곽 파악에 적합

  - `cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst`

    - **src** – Source image. The number of channels can be arbitrary. The depth should be one of `CV_8U`, `CV_16U`, `CV_16S`, `CV_32F` or ``CV_64F`.

    - op

      Type of a morphological operation that can be one of the following:

      - **MORPH_OPEN** - an opening operation
      - **MORPH_CLOSE** - a closing operation
      - **MORPH_GRADIENT** - a morphological gradient. Dilation과 erosion의 차이.
      - **MORPH_TOPHAT** - “top hat”. Opeining과 원본 이미지의 차이
      - **MORPH_BLACKHAT** - “black hat”. Closing과 원본 이미지의 차이

    - **kernel** – structuring element. `cv2.getStructuringElemet()` 함수로 만들 수 있음.

    - **anchor** – structuring element의 중심. default (-1,-1)로 중심점.

    - **iterations** – erosion and dilation 적용 횟수

    - **borderType** – Pixel extrapolation method. See `borderInterpolate` for details.

    - **borderValue** – Border value in case of a constant border. The default value has a special meaning.



- **Structuring Element**

  - `cv2.getStructuringElement(shape, ksize[, anchor]) -> retval`
    - shape - Element의 모양
      - **MORPH_RET** : 사각형 모양
      - **MORPH_ELLIPSE** : 타원형 모양
      - **MORPH_CROSS** : 십자 모양
    - ksize - structuring element 사이즈
  - Strucring Element 생성

  ```bash
  # numpy를 이용한 사각형 생성
  >>> import numpy as np
  >>> kernel = np.ones((5,5), np.uini8)
  
  # 함수를 사각형 이용한 생성
  >>> cv2.getStructuringElement(cv2.MORPH_REC,(5,5))
  array([ [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]], dtype=uint8)
          
  # 원 또는 타원 모양
  >>> cv2.getStructuringElement(cv2.MORP_ELLIPSE,(5,5))
  array([[0, 0, 1, 0, 0],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0]], dtype=uint8)
  ```

  

  - 예제 코드

  ```python
  import cv2
  from matplotlib import pyplot as plt
  
  img = cv2.imread('img/morph.png')
  
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
  #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
  #kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
  
  # erosion : 침식, dilation : 확장
  erosion = cv2.erode(img, kernel, iterations = 1)
  dilation = cv2.dilate(img, kernel, iterations = 1)
  
  # opening : erosion -> dilation
  opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
  # closing : dilation -> erosion
  closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
  # gradient : dilation과 erosion의 차이
  gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
  # tophat : opening과 원본의 차이
  tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
  # blackhat : closing과 원본의 차이
  blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
  
  images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]
  titles = ['image', 'erosion', 'dilation', 'opening', 'closing', 'gradient', 'tophat', 'blackhat']
  
  # plt 사이즈 조정
  plt.figure(figsize=(8,6))
  
  for i in range(len(images)):
      plt.subplot(3, 3, i+1), plt.imshow(images[i]), plt.title(titles[i])
      plt.xticks([]), plt.yticks([])
      
  plt.show()
  ```

  

![morph_result](img/morph_result.png)



### Image Gradients(기울기)

- image_gradients.py

- 목표
  - Edge Detection에 대해서 알 수 있다.
- Gradient(기울기)
  - 스칼라장(즉, 공간)에서 최대의 증가율을 나타내는 벡터장(방향과 힘)을 뜻함
  - 영상처리에서 gradient는 영상의 edge 및 그 방향을 찾는 용도로 활용이 됨
- **Sobel & Scharr Filter**
  - Gaussian smoothing과 미분을 이용한 방법
    - 노이즈가 있는 이미지에 적용하면 좋음
    - X축과 Y축을 미분하는 방법으로 경계값을 계산함
  - 직선을 미분하면 상수, 곡선을 미분하면 또 다른 방정식이 나오는 성질을 이용하여 edge에 대한 선을 그려주는 기능을 함
    - X축 미분은 수평선(수직선이 남음), Y축 미분은 수직선(수평선이 남음)을 미분하여 경계가 사라지는 효과가 있음
    - 미분시 소실되는 표본의 정보가 많을 수 있어 aperture_size 값을 이용하여 소실되는 정도를 조절할 수 있음
  - `cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst`
    - src - input image
    - ddepth - output image의 depth, -1이면 input image와 동일
    - dx - x축 미분지수
    - dy - y축 미분지수
    - ksize - kernel size(ksize x ksize)
  - `cv2.Scharr(src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]]) -> dst`
    - cv2.Sobel() 함수와 동일하나 ksize가 sobel의 3x3보다 좀 더 정확하게 적용이 됨
- **Laplacian 함수**
  - 이미지의 가로와 세로에 대한 Gradient를 2차 미분한 값
    - Sobel filter에 미분의 정도가 더해진 것과 비슷
  - blob(주위의 pixel과 확연한 pixel차이를 나타내는 덩어리)검출에 많이 사용됨
  - `cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst`
    - src - source image
    - ddepth - output image의 depth
- **Canny Edge Detection**
  - 가장 유명한 Edge Detection 방법
  - 여러 단계의 Algorithm을 통해서 경계를 찾아 냄
    1. Noise Reduction
       - 이미지의 Noise를 제거함. 이 때 5x5의 Gaussian filter를 이용함
    2. Edge Gradient Detection
       - 이미지에서 Gradient의 방향과 강도를 확인함
       - 경계값에서는 주변과 색이 다르기 때문에 미분값이 급속도로 변하게 됨
       - 이를 통해 경계값 후보군을 선별함
    3. Non-maximum Suppression
       - 이미지의 pixel을 Full scan하여 Edge가 아닌 pixel은 제거함
    4. Hysteresis Thresholding
       - 지금까지 Edge로 판단된 pixel이 진짜 edge인지 판별하는 작업을 함
       - max val과 min val(임계값)을 설정하여 max val이상은 강한 Edge, min과 max 사이는 약한 edge로 설정함
       - 약한 edge가 진짜 edge인지 확인하기 위해서 강한 edge로 연결되어 있으면 edge로 판단하고 그러지 않으면 제거함
  - `cv2.Canny(image, thresdhold1, threshold2[, edges[, apertureSize[, L2gradient]]]) -> edges`
    - image - 8 bit input images
    - threshold1 - Hysteresis Thresholding 작업에서의 min값
    - threshold2 - Hysteresis Thresholding 작업에서의 max값

![image_gradient_result](img/image_gradient_result.png)



### Image Pyramids

- image_pyramids.py

- 목표
  - Image Pyramid에 대해서 알 수 있다.
  - cv2.pyrUp() 와 cv2.pyrDown() 에 대해서 알 수 있다.

- Theory

  - 일반적으로는 고정된 이미지 사이즈를 작업을하지만, 때때로 동일한 이미지에 대해서 다양한 사이즈를 가지고 작업을 해야 하는 경우가 있음

    - 만일, 이미지에서 얼굴을 찾을 경우 얼굴의 사이즈를 확신할 수 없음
    - 이럴 경우에는 원본 이미지에 대한 다양한 사이즈에서 얼굴을 찾는다면 좀 더 정확하고 확실한 이미지를 찾을 수 있음

  - 동일 이미지의 서로 다른 사이즈의 set을 Image Pyramids라고 함

    - 가장 아래에 가장 큰 해상도를 놓고 점점 줄여가면서 쌓아가는 형태

  - 종류

    - Gaussian Pyramids
      - Gaussian Pyramid의 High Level(낮은 해상도. Pyramid의 상단)은 Lower level에서 row와 column을 연속적으로 제거하면서 생성됨.
      - MxN 사이즈의 이미지는 M/2 x N/2가 적용되면 1/4사이즈로 줄어들게 됨

    ```python
    import cv2
    
    img = cv2.imread('img/monkey.tiff')
    
    lower_reso = cv2.pyrDown(img)   # 원본 이미지의 1/4 사이즈
    higher_reso = cv2.pyrUp(img)    # 원본 이미지의 4배 사이즈
    
    cv2.imshow('img', img)
    cv2.imshow('lower', lower_reso)
    cv2.imshow('higher', higher_reso)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```

    

    - Laplacian Pyramids
      - cv2.pyrDown() 후에 cv2.pyrUP()을 적용하면 원본과 이미지 차이가 발생할 수 있음(홀수일때)
      - 이것을 resize를 통해 동일한 shape로 만든 후 원본과 이 이미지의 배열 차이를 구하면 외곽선이 남게됨(짝수 해상도도 마찬가지)

    ```python
    import cv2
    
    img = cv2.imread('img/monkey.tiff')
    print(img.shape) # (512, 512, 3)
    
    GAD = cv2.pyrDown(img)
    print(GAD.shape) # (256, 256, 3)
    
    GAU = cv2.pyrUp(GAD)
    print(GAU.shape) # (512, 512, 3)
    
    temp = cv2.resize(GAU, (512, 512))
    res = cv2.subtract(img, temp)
    
    cv2.imshow('res', res)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```

    

![lap_pyramids](img/lap_pyramids.png)





- 이미지 Pyrimids를 이용하면 이미지 결합을 자연스럽게 처리할 수 있음

- 작업 순서

  - 2개의 이미지를 각각 Load함
  - 각 이미지에 대해서 적당한 Gaussian Pyramid를 생성함
  - Gaussian Pyramid를 이용하여 Laplacian Pyramid를 생성함
  - 각 단계의 Laplicain Pyramid를 이용하여 각 이미지의 좌측과 우측을 결합
  - 결합한 결과중 가장 작은 이미지를 확대하면서 동일 사이즈의 결합결과와 Add하여 외곽선을 선명하게 처리함

  ```python
  import cv2
  import numpy as np
  
  STEP = 6
  
  # 1단계
  A = cv2.imread('img/apple.jpg')
  B = cv2.imread('img/orange.jpg')
  
  
  # 2단계
  # A 이미지에 대한 Gaussian Pyramid를 생성
  # 점점 작아지는 Pyramid
  G = A.copy()
  gpA = [G]
  for i in range(STEP):
      G = cv2.pyrDown(G)
      gpA.append(G)
      
  # B 이미지에 대한 Gaussian Pyramid 생성
  # 점점 작아지는 Pyramid
  G = B.copy()
  gpB = [G]
  for i in range(STEP):
      G = cv2.pyrDown(G)
      gpB.append(G)
      
      
  # 3단계
  # A 이미지에 대한 Laplacian Pyramid 생성
  lpA = [gpA[STEP-1]]  # n번쨰 추가된 Gaussian Image
  for i in range(STEP-1, 0, -1):
      GE = cv2.pyrUp(gpA[i])
      L = cv2.subtract(gpA[i-1], GE)
      lpA.append(L)
      
  # B 이미지에 대한 Laplacian Pyramid 생성
  lpB = [gpB[STEP-1]]
  for i in range(STEP-1, 0, -1):
      GE = cv2.pyrUp(gpB[i])
      L = cv2.subtract(gpB[i-1], GE)
      lpB.append(L)
     
      
  # 4단계
  # Laplacian Pyramid를 누적으로 좌측과 우측으로 재결합
  LS = []
  for la, lb in zip(lpA, lpB):
      rows, cols, dpt = la.shape
      ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))
      LS.append(ls)
      
      
  # 5단계
  ls_ = LS[0] # 좌측과 우측이 합쳐진 가장 작은 이미지
  for i in range(1, STEP):
       ls_ = cv2.pyrUp(ls_)    # Up scale
       ls_ = cv2.add(ls_, LS[i]) # Up Scale된 이미지에 외곽서늘 추가하여 선명한 이미지로 생성
      
  # 원본 이미지를 그대로 붙인 경우
  real = np.hstack((A[:, :int(cols/2)], B[:, int(cols/2):]))
  
  cv2.imshow('real', real)
  cv2.imshow('blending', ls_)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
  ```





### Image Contours(이미지 윤곽)

- 목표
  - Contours에 대해서 알 수 있다.
  - cv2.findContours(), cv2.drawContours() 함수에 대해서 알 수 있다.
- **Contours**
  - 



### Contour Feature



### Contour Property



### Contours Hierarchy



### 히스토그램



### 히스토그램 균일화



### 2D Histogram



### 푸리에 변환



### 템플릿 매칭



### 허프 변환

