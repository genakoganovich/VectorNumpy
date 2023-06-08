import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


a = np.array(input().split()).astype(float)

print(*round_v(np.rad2deg(np.arccos(np.multiply(1 / np.linalg.norm(a), a)))))
