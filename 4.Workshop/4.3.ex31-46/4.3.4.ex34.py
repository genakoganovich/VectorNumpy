import numpy as np


def round_v(v):
    return np.round(v, 2)


mod_a, mod_b, a_deg = [float(input()) for i in range(3)]

print(round_v(mod_a ** 2 * mod_b ** 2 * (1 - np.cos(np.deg2rad(a_deg)) ** 2)))
