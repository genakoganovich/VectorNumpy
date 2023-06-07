import numpy as np


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

norm_rows = np.linalg.norm(A, ord=2, axis=1)

print(*norm_rows)
