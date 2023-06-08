import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


A, B = [np.array(input().split()).astype(float) for i in range(2)]

AB = np.subtract(B, A)

print(round_v(A + np.multiply(1 / 3, AB)))
print(round_v(A + np.multiply(2 / 3, AB)))
