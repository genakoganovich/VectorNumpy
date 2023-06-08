import numpy as np


def round_v(v):
    return np.round(v, 2)


p, q, r, a = [np.array(input().split()).astype(float) for i in range(4)]
print(round_v(np.linalg.solve(np.column_stack([p, q, r]), a)))
