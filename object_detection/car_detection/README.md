## 객체 탐지

### 차량 탐지

- [링크](<https://medium.com/machine-learning-world/tutorial-making-road-traffic-counting-app-based-on-computer-vision-and-opencv-166937911660>)

- 딥러닝 이용 x
- 자동차만 있다고 가정 했을 때 움직이는 물체에 대한 탐지

#### 필요 패키지

- skvideo.io

  - `pip install sk-video`
  - 사용법

  ```python
  import skvideo.io
  
  vid = skvideo.io.vread('sample.mp4') # 비디오를 읽어옴
  vid.shape # (프레임 수, Y, X, channels)
  
  for i, shortcut in enumerate(vid): # 각 프레임 조회
  print shortcut # example code
  ```

  

#### 필요기능

- 배경화면 추출
- 필터링