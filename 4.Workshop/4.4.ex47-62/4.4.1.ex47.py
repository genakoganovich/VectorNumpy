import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


a, b = [np.array(input().split()).astype(float) for i in range(2)]

print(round_v(proj(b, a)))
print(round_v(np.rad2deg(np.arccos(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))))))
