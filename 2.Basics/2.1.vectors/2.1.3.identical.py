import numpy as np

a, b = [np.array(list(map(int, input().split()))) for _ in range(2)]

print(np.all(a[3:] - a[:3] == b[3:] - b[:3]))
