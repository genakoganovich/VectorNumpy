import numpy as np

a, b, c = [np.array(input().split()).astype(float) for i in range(3)]
print(not np.dot(a, np.cross(b, c)))
