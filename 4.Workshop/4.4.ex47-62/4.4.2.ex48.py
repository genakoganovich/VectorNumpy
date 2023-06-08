import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


c = np.array(input().split()).astype(float)
mod_p = float(input())

print(round_v(np.multiply(-mod_p / np.linalg.norm(c), c)))
