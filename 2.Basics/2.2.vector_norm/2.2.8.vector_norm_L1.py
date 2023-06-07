import numpy as np

n = int(input())
v = np.array([pow(0.5, i) for i in range(1, n + 1)])
norm_l1 = np.linalg.norm(v, ord=1)
print(norm_l1)
