import numpy as np


v = np.array([2, -5, 1, 7, -3, 0])
norm_inf = np.linalg.norm(v, ord=np.inf)
print(norm_inf)
