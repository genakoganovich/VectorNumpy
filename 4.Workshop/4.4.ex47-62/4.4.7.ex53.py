import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


A, B, C, D = [np.array(input().split()).astype(float) for i in range(4)]
AB = np.subtract(B, A)
AC = np.subtract(C, A)
AD = np.subtract(D, A)


print(not np.dot(AB, np.cross(AC, AD)))
