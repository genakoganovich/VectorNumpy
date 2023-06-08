import numpy as np


def round_v(v):
    return np.round(v, 2)


a, b, c = [np.array(input().split()).astype(float) for i in range(3)]
print(round_v(np.dot(a, b)))
print(round_v(np.cross(a, b)), round_v(np.linalg.norm(np.cross(a, b))))
print(round_v(np.dot(a, np.cross(b, c))))
print(round_v(np.cross(a, np.cross(b, c))), round_v(np.linalg.norm(np.cross(a, np.cross(b, c)))))
