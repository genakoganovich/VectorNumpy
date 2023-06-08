import numpy as np

a, b = [np.array(input().split()).astype(float) for i in range(2)]
print(*np.round(np.cross(a, b), 2))
