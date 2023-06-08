import numpy as np

a, b, c = [np.array(input().split()).astype(float) for i in range(3)]
print(np.cross(a, np.cross(b, c)))
