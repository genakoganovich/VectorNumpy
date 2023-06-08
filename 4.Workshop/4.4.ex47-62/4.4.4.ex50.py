import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


a, b, c = [np.array(input().split()).astype(float) for i in range(3)]
N = float(input())

print(round_v(np.linalg.solve(np.array([a, b, c]), np.array([0, 0, N]))))
