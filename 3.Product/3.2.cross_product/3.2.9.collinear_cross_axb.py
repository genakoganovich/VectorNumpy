import numpy as np

a, b = [np.array(input().split()).astype(float) for i in range(2)]
print(False if np.cross(a, b).all() else True)
