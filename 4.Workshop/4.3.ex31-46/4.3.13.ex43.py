import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


a, b = [np.array(input().split()).astype(float) for i in range(2)]
mod_c = float(input())

k = np.array([0, 0, 1])
axb = np.cross(a, b)
norm_axb = np.linalg.norm(axb)

print(round_v(axb * mod_c / norm_axb) if np.dot(axb, k) < 0 else -round_v(axb * mod_c / norm_axb))
