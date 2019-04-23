import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)   # 정규분포로 초기화
        
    def predict(self, x):
        return np.dot(x, self.W)
    
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        
        return loss
    
x = np.array([0.6, 0.9])
# 정답 레이블
t = np.array([0, 0, 1])

net = simpleNet()

# 손실 함수를 계산하는 함수
f = lambda w: net.loss(x, t)
# 위의 함수를 편미분한 값 -> 신경망의 기울기
dW = numerical_gradient(f, net.W)

print(dW)