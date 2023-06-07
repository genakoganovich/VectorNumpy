import numpy as np

a, b = [np.array(list(map(float, input().split()))) for _ in range(2)]
print(np.linalg.norm(np.multiply(3, a) - np.multiply(2, b)))
