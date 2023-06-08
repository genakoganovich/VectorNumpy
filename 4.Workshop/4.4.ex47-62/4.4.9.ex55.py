import math

import numpy as np


def round_v(v):
    return np.round(v, 2)


def proj(u, v):
    return np.dot(u, v) / np.linalg.norm(v)


mod_a = float(input())
angle_x, angle_y = map(float, input().split())

print(round_v(np.rad2deg(np.arccos(
    np.sqrt(abs(1 - np.cos(np.deg2rad(angle_x)) ** 2 - np.cos(np.deg2rad(angle_y)) ** 2))))))
