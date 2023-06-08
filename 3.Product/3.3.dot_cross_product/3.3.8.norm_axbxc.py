import numpy as np

a, b, c = [np.array(input().split()).astype(float) for i in range(3)]
print(round(np.linalg.norm(np.cross(a, np.cross(b, c))), 2))
