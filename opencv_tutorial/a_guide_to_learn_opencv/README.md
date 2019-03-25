## 참조링크

- <https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/>



## Tutorial-1

- OpenCV는 픽셀 값이 일반적인 RGB 포맷이 아닌 BGR로 되어 있음

- - 매우 오래전에 개발된 프로그램이기 때문

```python
# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB

(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))
```



- 이미지 자르기

- - "regions of interest(ROIs)"를 추출하는 것은 이미지 처리에서 중요한 스킬이다.
  - 예) 얼굴인식

```python
# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160

roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
```



- 이미지 사이즈 조정하기

```python
# resize the image to 200x200px, ignoring aspect ratio

resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)
```



- - 같은 비율로 줄이기

```python
# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio

r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)
```



- - 같은 비율 줄이기(imutils.resize 이용)

```python
# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead

resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)
```





- 이미지 회전하기

- - 반시계 방향으로 45도 회전

```python
# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp

center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)
```



- - imutils 이용

```python
# rotation can also be easily accomplished via imutils with less code

rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

```

- - 잘린 이미지까지 다 보여주기

```python
# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out

rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)
```



- 이미지 매끄럽게 하기

```python
# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise

blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
```



- 이미지에 그리기

- - 사각형 그리기

  - - rectangle 인수
    - (1)원본 이미지, (2)왼쪽 위 지점, (3)오른쪽 아래 지점, (4)선의 BGR 색, (5) 두께

```python
# draw a 2px thick red rectangle surrounding the face

output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)
```



- - 파란색 원 그리기

  - - circle 인수

    - (1)원본 이미지, (2)원의 중심점, (3)원의 반지름, (4)선의 BGR 색, (5) 두께

    - - 두께가 -1일 경우 전부 채움

```python
# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150

output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)
```



- - 빨간 선 그리기

```python
# draw a 5px thick red line from x=60,y=20 to x=400,y=200

output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)
```



- - 녹색 텍스트 작성하기

  - - putText 인수
    - (1)원본 이미지, (2)텍스트, (3)폰트 시작점
    - (4)폰트, (5)글꼴 크기, (6)글자 색, (7)두께

```python
# draw green text on the image

output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25),
cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
```





## Tutorial-2

- 필요 패키지 호출 및 인수 설정

- - argparse를 통해 터미널에서 입력해야 하는 변수 설정

  - - args["image"]를 통해 입력한 인수에 접근할 수 있음

```python
# import the necessary packages

import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="path to input image")
args = vars(ap.parse_args())


```



- 회색으로 이미지 변환

```python
# load the input image (whose path was supplied via command line
# argument) and display the image to our screen

image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# convert the image to grayscale

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
```





- 가장자리 감지

- - 이미지에 있는 객체의 경계를 찾는데 유용
  - Canny 인수
  - (1)원본 이미지, (2)최소 임계값(threshold), (3)최대 임계값

```python
# applying edge detection we can find the outlines of objects in
# images

edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
```





- Thresholding(임계값)

- - 이미지 thresholding은 이미지 처리 파이프라인의 중요한 중간 단계임

  - Thresholding은 밝은 영역이나 어두운 영역 및 윤곽을 제거하는데 도움이 될 수 있음

  - - 225 보다 높은 픽셀은 0(black)으로 만듬
    - 225에서 255까지 값은 보이기

```python
# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
```





- 윤곽선 감지 및 그리기

```python
# find contours (i.e., outlines) of the foreground objects in the
# thresholded image

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

# loop over the contours

for c in cnts:
    # draw each contour on the output image with a 3px thick purple
    # outline, then display the output contours one at a time
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Contours", output)
	cv2.waitKey(0)
```



- - 텍스트 작성하기

```python
# draw the total number of contours found in purple

text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)
```





- 축소와 확대

- - 축소(erode)

```python
# we apply erosions to reduce the size of foreground objects

mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)
```



- - 확대(dilate)

```python
# similarly, dilations can increase the size of the ground objects

mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)
```



- 마스킹 및 비트 연산

- - 마스킹 된 테트리스 블록만 보이도록 함

```python
# a typical operation we may want to apply is to take our mask and
# apply a bitwise AND to our input image, keeping only the masked
# regions

mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)
```

