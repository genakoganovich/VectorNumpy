import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


A, B, D = [np.array(input().split()).astype(float) for i in range(3)]

AB = np.subtract(B, A)
AD = np.subtract(D, A)
BD = np.subtract(D, B)
AC = AB + AD

print(round_v(np.rad2deg(np.arccos(np.dot(AC, BD) / (np.linalg.norm(AC) * np.linalg.norm(BD))))))
