import numpy as np


def round_v(v):
    return np.round(v, 2)


a, b = [np.array(input().split()).astype(float) for i in range(2)]

print(not np.any(np.cross(a, b)))
print(round_v(np.linalg.norm(a) / np.linalg.norm(b)))
print(np.dot(a, b) < 0 and not np.any(np.cross(a, b)))
