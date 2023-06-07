import numpy as np

a_coordinates, b_coordinates = [np.array(list(map(float, input().split()))) for _ in range(2)]

a = a_coordinates[2:] - a_coordinates[:2]
b = b_coordinates[2:] - b_coordinates[:2]

print(np.linalg.norm(a + b))
