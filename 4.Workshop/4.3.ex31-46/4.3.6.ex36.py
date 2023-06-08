import numpy as np


def round_v(v):
    return np.round(v, 2)


mod_a, mod_b, a_deg = [float(input()) for i in range(3)]

print(round_v(4 * mod_a * mod_b * np.sin(np.deg2rad(a_deg))))
