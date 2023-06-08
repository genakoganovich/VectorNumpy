import numpy as np


def round_v(v):
    return np.round(v, 2)


F, A = [np.array(input().split()).astype(float) for i in range(2)]

print(round_v(np.cross(A, F)))
