import numpy as np
import matplotlib.pylab as plt

def function_1(x):
    return 0.01*x**2 + 0.1*x


def numerical_diff(f, x):
    h = 1e-4    # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y


if __name__ == "__main__":
    x = np.arange(0.0, 20.0, 0.1)   # 0에서 20까지 0.1 간격의 배열 x를 만든다
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")

    tf = tangent_line(function_1, 5)
    y2 = tf(x)

    plt.plot(x, y)
    plt.plot(x, y2)
    plt.show()

    print(numerical_diff(function_1, 5))    # 0.1999999999990898
    print(numerical_diff(function_1, 10))   # 0.2999999999986347

