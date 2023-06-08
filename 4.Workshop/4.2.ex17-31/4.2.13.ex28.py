import numpy as np


def round_v(v):
    return np.round(v, 2)


a, b, A = [np.array(input().split()).astype(float) for i in range(3)]
print(*round_v(A + (a + b) / 3))
