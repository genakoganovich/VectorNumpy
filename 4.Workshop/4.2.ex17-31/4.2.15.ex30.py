import numpy as np


def round_v(v):
    return np.round(v, 2)


a, b, c = [np.array(input().split()).astype(float) for i in range(3)]
print(round_v(np.dot(np.multiply(2, a) - b, c)))
