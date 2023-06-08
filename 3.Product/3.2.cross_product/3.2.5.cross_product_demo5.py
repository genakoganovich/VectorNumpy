import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]])

print(np.cross(x, y))
print(np.cross(x, y, axisa=0, axisb=0))
