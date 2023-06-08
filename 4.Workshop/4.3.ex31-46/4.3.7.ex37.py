import numpy as np


def round_v(v):
    return np.round(v, 2)


a, b = [np.array(input().split()).astype(float) for i in range(2)]

print(*round_v(np.array([np.linalg.norm(a + b), np.linalg.norm(a - b), np.linalg.norm(np.cross(a, b))])))
