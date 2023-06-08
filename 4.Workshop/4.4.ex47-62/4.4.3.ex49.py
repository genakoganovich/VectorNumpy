import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


A, B, C = [np.array(input().split()).astype(float) for i in range(3)]
AB = np.subtract(B, A)
AC = np.subtract(C, A)
BC = np.subtract(C, B)

print(round_v(np.linalg.norm(np.cross(AB, AC)) / np.linalg.norm(BC)))
