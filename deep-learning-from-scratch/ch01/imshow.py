import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../dataset/lena.jpg')

plt.imshow(img)
plt.show()