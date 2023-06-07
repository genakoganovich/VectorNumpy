import numpy as np

a, b = [np.array(input().split()).astype(float) for i in range(2)]
c1 = np.add(a, b)
c2 = np.subtract(a, b)
c3 = np.multiply(-2, a)
c4 = np.multiply(0.5, b)


def solve_1(v):
    return round(np.linalg.norm(v), 2)


def solve_2(v):
    return np.round(np.multiply(1 / np.linalg.norm(v), v), 2)


print(solve_1(a), solve_1(c1), solve_1(c4 + c3))
print(solve_2(b), solve_2(c2))
