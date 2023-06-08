import numpy as np


def round_v(v):
    return np.round(v, 2)


A, B, C = [np.array(input().split()).astype(float) for i in range(3)]

BC = np.subtract(C, B)
CA = np.subtract(A, C)
CB = np.subtract(B, C)

print(round_v(BC - 2 * np.cross(CA, CB)))
