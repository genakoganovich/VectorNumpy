import numpy as np

a, b = [np.array(input().split()).astype(float) for i in range(2)]
print(round(np.linalg.norm(np.cross(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))), 2))
