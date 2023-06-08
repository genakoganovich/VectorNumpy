import numpy as np


def round_v(v):
    return np.round(v, 2)


cos_a = np.cos(np.deg2rad(list(map(float, input().split()))))
print(np.linalg.norm(cos_a) == 1)
