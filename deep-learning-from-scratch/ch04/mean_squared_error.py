import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

if __name__ == "__main__":
    # 정답은 '2'
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

    # 예1 : '2'일 확률이 가장 높다고 추정함 (0.6)
    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    result1 = mean_squared_error(np.array(y), np.array(t))  # 0.09750000000000003
    print(f'result1: {result1}')

    # 예2 : '7'일 확률이 가장 높다고 추정함 (0.6)
    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    result2 = mean_squared_error(np.array(y), np.array(t))  # 0.5975
    print(f'result2: {result2}')
