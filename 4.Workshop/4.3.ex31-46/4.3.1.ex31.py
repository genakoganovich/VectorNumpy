import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


A, B, C = [np.array(input().split()).astype(float) for i in range(3)]

CA = np.subtract(A, C)
CB = np.subtract(B, C)
print(round_v(np.rad2deg(np.arcsin(np.linalg.norm(np.cross(CA, CB))/ (np.linalg.norm(CA) * np.linalg.norm(CB))))))
