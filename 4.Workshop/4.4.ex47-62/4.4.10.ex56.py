import math

import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


A, B, C, D = [np.array(input().split()).astype(float) for i in range(4)]

BC = np.subtract(C, B)
DA = np.subtract(A, D)

print(not np.any(round_v(np.cross(BC, DA))) and np.linalg.norm(BC) != np.linalg.norm(DA))

