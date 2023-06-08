import numpy as np


def round_v(v):
    return np.round(v, 2)


def length(v):
    return np.linalg.norm(v)


A, B, C, D = [np.array(input().split()).astype(float) for i in range(4)]

AB = np.subtract(B, A)
BC = np.subtract(C, B)
CD = np.subtract(D, C)
DA = np.subtract(A, D)

print(np.all(np.array([length(AB), length(BC), length(CD)]) == length(DA)) and not np.dot(AB, BC) and not np.dot(BC, CD))
