import numpy as np

a, b = [np.array(input().split()).astype(float) for i in range(2)]
k = int(input())

ab = np.subtract(b, a)
ac = a + np.multiply(k / (1 + k), ab)

print(*ac)
