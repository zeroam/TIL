import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

if __name__ == "__main__":
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    r1 = cross_entropy_error(np.array(y), np.array(t))
    print(f'r1:{r1}')   # r1:0.510825457099338

    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    r2 = cross_entropy_error(np.array(y), np.array(t))
    print(f'r2:{r2}')   # r2:2.302584092994546
