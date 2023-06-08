import numpy as np


def round_v(v):
    return np.round(v, 2)


A, B, a = [np.array(input().split()).astype(float) for i in range(3)]
AB = np.subtract(B, A)

print(round_v(AB))
print(round_v(np.linalg.norm(AB)))
print(round_v(np.multiply(1 / np.linalg.norm(AB), AB)))
print(round_v(B + a))
