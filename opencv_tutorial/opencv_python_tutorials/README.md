## 참조링크

- [한글 번역본](<https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html>)
- [영문 원본](<https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#goals>)



## 튜토리얼

### 이미지 다루기

- images.py
- 목표
  - cv2.imread(), cv2.imshow(), cv2.imwrite()에 대해 배우기
  - 이미지 읽기, 나타내기, 저장하기
  - Matplotlib으로 이미지 나타내기

- 이미지 읽기
  - `cv2.IMREAD_COLOR` (1)
    - 이미지 파일을 Color으로 읽어들임. 투명한 부분은 무시되며, Default 값임
  - `cv2.IMREAD_GRAYSCALE` (0)
    - 이미지를 Grayscale로 읽어들임. 실제 이미지 처리시 중간단계로 많이 사용함
  - `cv2.IMREAD_UNCHANGED` (-1)
    - 이미지파일을 alpha channel까지 포함하여 읽어들임
- 이미지 보기
  - `cv2.imshow(title, image)`
    - 이미지를 사이즈에 맞게 보여줌
    - title (str) - 윈도우 창의 title
    - image - cv2.imread()의 return 값
  - `cv2.waitKey(time)`
    - keyboard 입력을 대기하는 함수로 0이면 key입력까지 무한 대기
    - 특정시간까지 대기하려면 millisecond 값을 넣어주면 됨
  - `cv2.destroyAllWindows()`
    - 화면에 나타난 모든 윈도우를 제거함
  - `cv2.destroyWindow(title)`
    - 특정 윈도우를 제거함
    - 인자값으로 윈도우 이름을 입력해야 함
  - `cv2.namedWindow(title, flag)`
    - title (str) - 윈도우 창의 title
    - flag
      - cv2.WINDOW_AUTOSIZE : 원래 이미지 사이즈, 사이즈 조정 x
      - cv2.WINDOW_NORMAL : 원래 이미지 사이즈, 사이즈 조정 O
- 이미지 저장하기
  - `cv2.imwrite(fileName, image)`
    - fileName (str) - 저장될 파일명
    - image - 저장할 이미지 
- Matplotlib 사용하기
  - Matplotlib는 다양한 plot 기능을 가진 Python plotting library
  - 하나의 화면에 여러 개의 이미지를 보고자 할 때 유용



### 영상 다루기

- videos.py

- 목표

  - 동영상 읽기, 보여주기, 저장하기
  - cv2.VideoCapture(), cv2.VideoWrite() 함수 배우기

- 카메라로 부터 비디오 캡쳐하기

  - 순서

  1. VideoCapture Object 생성. 변수로는 camera device index나 동영상 파일명을 넘겨줌. 일반적으로 0이면 Camera와 연결이 됨
  2. Loop을 돌면서 frame을 읽어들임
  3. 읽은 frame에 대해서 변환작업을 수행한 후, 화면에 보여줌
  4. 영상 재생이 끝나면, VideoCapture Object를 release하고 window를 닫음

  - `cv2.VideoCapture()`
    - VideoCapture Object 생성
    - 인자로 0을 보냄, 인자 값은 비디오 파일의 인덱스 값으로 설정됨
    - 두번째 카메라를 선택할 때는 1, ...을 인자값으로 입력
  - cap.read()
    - 프레임이 정확하게 읽어 지는지에 대한 결과 값을 bool(True/False)으로 나타내줌 -> 리턴값을 통해 실행여부를 확인할 수 있음
  - cap.isOpened()
    - capture가 초기화 되지 않은 경우 cap.isOpened()를 통해 확인할 수 있고, cap.open()으로 초기화 할 수 있음

- 파일(File)로 부터 영상 재생하기

  - `cv2.VideoCapture(videofile)`
    - videofile (str) : 영상 파일명

- 영상 저장하기

  - `cv2.VideoWriter(outputFile, fourcc, frame, size)`
    - outputFile (str) - 저장될 파일명
    - fourcc - Codec정보, cv2.VideoWriter_fourcc()
    - frame (float) - 초당 저장될 frame
    - size (list) - 저장될 사이즈(ex.640, 480)
  - Windows는 DIVX 코덱 지원



### 도형 그리기

- drawing_functions.py

- 목표

  - 다양한 모양의 도형을 그릴 수 있음
  - cv2.line(), cv2.circle(), cv2.rectangle, cv2.putText() 사용법을 알 수 있음

- Line 그리기

  - `cv2.line(img, start, end, color, thickness)`
    - img - 그림을 그릴 이미지 파일
    - start - 시작 좌표(ex; (0, 0))
    - end - 종료 좌표(ex; (500, 500))
    - color - BGR 형태의 Color(ex; (255, 0, 0) -> Blue)
    - thickness (int) - 선의 두께, pixel

- 사각형 그리기

  - `cv2.rectangle(img, start, end, color, thickness)`
    - img - 그림을 그릴 이미지
    - start - 시작 좌표(ex; (0, 0))
    - end - 종료 좌표(ex; (500, 500))
    - color - BGR 형태의 Color(ex; (255, 0, 0) -> Blue)
    - thickness (int) - 선의 두께, pixel

- 원 그리기

  - `cv2.circle(img, center, radian, color, thickness)`
    - img - 그림을 그릴 이미지
    - center - 원의 중심 좌표(x, y)
    - radian - 반지름
    - color - BGR 형태의 Color
    - thickness - 선의 두께, -1 이면 원의 안쪽을 채움

- 타원 그리기

  - `cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness])`
    - img - 그림을 그릴 이미지
    - center - 타원의 중심
    - axes - 중심에서 가장 큰 거리와 작은 거리
    - angle - 타원의 기울기 각
    - startAngle - 타원의 시작 각도
    - endAngle - 타원이 끝나는 각도
    - color - 타원의 색
    - thickness - 선 두께 -1이면 안쪽을 채움

- Polygon 그리기

  - `cv2.polylines(img, pts, isClosed, color, thisckness)`
    - img - 그림을 그릴 이미지
    - pts (array) - 연결할 꼭지점 좌표
    - isClosed - 닫힌 도형 여부
    - color - BGR 형태의 Color
    - thickness - 선 두께

- 이미지에 Text 추가

  - `cv2.putText(img, text, org, font, fontScale, color, thickness)`

    - img - 그림을 그릴 이미지

    - text - 표시할 문자열

    - org - 문자열이 표시될 위치. 문자열의 bottom-left corner 점

    - font - 폰트 타입, CV2.FONT_XXX

      - cv2.putText() 문서 참조

    - fontScale - 폰트 크기

      



### Mouse로 그리기

- mouse_as_the_color_palette.py
- 목표
  - Mouse Event의 적용 방법을 알 수 있음
  - cv2.setMouseCallback() 함수에 대해 배움

- 마우스 이벤트 목록 확인하기
  - 다양한 Mouse Event의 종류를 알 수 있음

```python
import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
```

- `cv2.setMouseCallback(windowName, callback, param=None)`

  - windowName - windowName
  - callback - callback 함수, callback 함수에는 (event, x, y, flags, param)이 전달됨.
  - param - callback 함수에 전달되는 Data

- 간단한 Demo(Simple Demo)

  - 화면에 Double-Click을 하면 원이 그려지는 예제

  ```python
  import cv2
  import numpy as np
  
  # callback 함수
  def draw_circle(event, x, y, flags, param):
      if event == cv2.EVENT_LBUTTONDBLCLK:
          cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
          
  # 빈 이미지 생성
  img = np.zeros((512, 512, 3), np.uint8)
  cv2.namedWindow('image')
  cv2.setMouseCallback('image', draw_circle)
  
  while(1):
      cv2.imshow('image', img)
      if cv2.waitKey(20) & 0xFF == 27:
          break
      
  cv2.destroyAllWindows()
  ```

- Advanced Demo

  - 마우스를 누른 상태에서 이동시 원 또는 사각형을 그리는 Demo

  ```python
  import cv2
  import numpy as np
  
  drawing = False     # Mouse가 클릭된 상태 확인
  mode = True         # True이면 사각형, False면 원
  ix, iy = -1, -1
  
  # mouse callback 함수
  def draw_circle(event, x, y, flags, param):
      global ix, iy, drawing, mode
      
      if event == cv2.EVENT_LBUTTONDOWN:  # 마우스를 누른 상태
          drawing = True
          ix, iy = x, y
      elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동
          if drawing == True:     # 마우스를 누른 상태일 경우
              if mode == True:
                  cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
              else:
                  cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
      elif event == cv2.EVENT_LBUTTONUP:
          drawing = False
          if mode == True:
              cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
          else:
              cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
              
  img = np.zeros((512, 512, 3), np.uint8)
  cv2.namedWindow('image')
  cv2.setMouseCallback('image', draw_circle)
  
  while True:
      cv2.imshow('image', img)
      
      k = cv2.waitKey(1) & 0xFF
      if k == ord('m'):   # 사각형, 원 Mode 변경
          mode = not mode
      elif k == 27:       # Esc 누르면 종료
          break
      
  cv2.destroyAllWindows()
  ```

  







### Trackbar



### Basic Operation



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