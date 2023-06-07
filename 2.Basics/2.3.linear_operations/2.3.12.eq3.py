import numpy as np

a = np.array('3 -5 2'.split()).astype(float)
b = np.array('5 -3 1'.split()).astype(float)


k = 0.5
print(*np.round((b - (b - a) / (k + 1)), 2))
k = 2
print(*np.round((b - (b - a) / (k + 1)), 2))
