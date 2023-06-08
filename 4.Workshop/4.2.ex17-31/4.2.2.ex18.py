import numpy as np


def round_v(v):
    return np.round(v, 2)


norm_a = float(input())
cos_a = np.cos(np.deg2rad(list(map(float, input().split()))))
print(*round_v(np.multiply(norm_a, cos_a)))
