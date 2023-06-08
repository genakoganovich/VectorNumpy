import numpy as np


def round_v(v):
    return np.round(v, 2)


A, B, C, D = [np.array(input().split()).astype(float) for i in range(4)]

AB = np.subtract(B, A)
AC = np.subtract(C, A)
AD = np.subtract(D, A)

print(abs(round_v(np.dot(AB, np.cross(AC, AD)) / 6)))
