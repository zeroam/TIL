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



### Mouse로 그리기



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