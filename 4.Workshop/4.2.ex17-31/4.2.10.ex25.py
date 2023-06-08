import numpy as np


a, b, c = [np.array(input().split()).astype(float) for i in range(3)]
print(np.any(np.cross(b, c)), np.any(np.cross(a, c)), np.any(np.cross(a, b)))
