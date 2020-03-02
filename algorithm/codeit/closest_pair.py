"""
태호가 사용하려는 함수 closest_pair는 이 좌표 리스트를 파라미터로 받고,
리스트 안에서 가장 가까운 두 매장을 [(x1, y1), (x2, y2)] 형식으로 리턴합니다.

참고로 태호는 이미 두 좌표 사이의 거리를 계산해 주는 함수 distance를 써 놨는데요,
함수 distance는 인풋으로 두 튜플을 받아서 그 사이의 직선 거리를 리턴합니다.
"""

# 제곱근 사용을 위한 sqrt 함수
import sys
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    min_distance = sys.maxsize
    result = list()
    for spot_a in coordinates:
        for spot_b in coordinates:
            if spot_a is spot_b:
                continue
            ab_distance = distance(spot_a, spot_b)
            if ab_distance < min_distance:
                min_distance = ab_distance
                result = [spot_a, spot_b]
    return result

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))