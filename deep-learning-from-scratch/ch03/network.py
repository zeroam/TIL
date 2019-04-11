import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def identity_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])    # 1층 가중치(2x3)
    network['b1'] = np.array([0.1, 0.2, 0.3])                       # 1층 편향(3)
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])  # 2층 가중치(3x2)
    network['b2'] = np.array([0.1, 0.2])                            # 2층 편향(2)
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])              # 3층 가중치(2x2)
    network['b3'] = np.array([0.1, 0.2])                            # 3층 편향(2)

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)            # 활성화 함수(시그모이드)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)            # 활성화 함수(시그모이드)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)   # 출력층의 활성화 함수

    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)    # [0.31682708 0.69627909]