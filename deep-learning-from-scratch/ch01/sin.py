import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)
plt.show()