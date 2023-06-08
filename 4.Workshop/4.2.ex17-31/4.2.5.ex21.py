import numpy as np


def round_v(v):
    return np.round(v, 2)


proj = np.array(input().split()).astype(float)
print(round_v(np.linalg.norm(proj)))
print(round_v(np.rad2deg(np.arccos(np.multiply(1 / np.linalg.norm(proj), proj)))))
