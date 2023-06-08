import numpy as np


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

x = np.array([a, b])
y = np.array([b, a])

print(np.cross(a, b))
print(np.cross(b, a))
print(np.cross(x, y))


