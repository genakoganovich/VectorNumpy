import math

import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


a, b, c = [np.array(input().split()).astype(float) for i in range(3)]

print(round_v(np.linalg.solve(np.column_stack([a, b]), a + b + c)))
