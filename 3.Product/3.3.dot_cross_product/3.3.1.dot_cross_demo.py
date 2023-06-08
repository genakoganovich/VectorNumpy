import numpy as np

# Векторы A, B и C
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])

# Вычисление смешанного произведения
result = np.dot(A, np.cross(B, C))

# Вывод результата
print("Смешанное произведение: ", result)
