import numpy as np


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


v = np.array([1, 2, 3])
print(np.linalg.norm(v, ord=None))
print(np.linalg.norm(v, ord=1))
print(np.linalg.norm(v, ord=2))
