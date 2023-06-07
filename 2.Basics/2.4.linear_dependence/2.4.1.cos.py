import numpy as np

a = np.array(input().split(), dtype=float)
norm = np.linalg.norm(a)
print(*np.round(np.multiply(1 / norm, a), 2))
