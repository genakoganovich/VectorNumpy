import numpy as np


def round_v(v):
    return np.round(v, 2)


mod_a, mod_b, a_dot_b = [float(input()) for i in range(3)]

print(round_v(mod_a * mod_b * np.sin(np.arccos(a_dot_b / (mod_a * mod_b)))))
