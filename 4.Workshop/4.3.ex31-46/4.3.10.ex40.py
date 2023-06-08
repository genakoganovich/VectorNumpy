import numpy as np


def round_v(v):
    return np.round(v, 2)


b, c, d = [np.array(input().split()).astype(float) for i in range(3)]

print('вектора некомпланарны' if np.dot(b, np.cross(c, d)) else 'вектора компланарны')
