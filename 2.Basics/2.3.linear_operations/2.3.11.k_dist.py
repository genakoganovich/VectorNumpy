import numpy as np

a, b = np.array(input().split(), dtype=float), np.array(input().split(), dtype=float)
k = int(input())
print(*(b - (b - a) / (k+1)))
