import numpy as np


def round_v(v):
    return np.round(v, 2)


A, B = [np.array(input().split()).astype(float) for i in range(2)]
AB = np.subtract(B, A)
print(round_v(np.multiply(1 / np.linalg.norm(AB), AB)))
