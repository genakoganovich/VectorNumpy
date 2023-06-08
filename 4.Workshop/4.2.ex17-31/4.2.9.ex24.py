import numpy as np


def round_v(v):
    return np.round(v, 2)


a, p, q = [np.array(input().split()).astype(float) for i in range(3)]
print(*round_v(np.linalg.solve(np.column_stack([p, q]), a)))
