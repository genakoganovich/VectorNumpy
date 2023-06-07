import numpy as np

# Создаемдвумерный массив
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Вычисляем модуль каждого столбца матрицы
norm_cols = np.linalg.norm(A, axis=0)
print(norm_cols)  # [ 8.1240384  9.64365076 11.22497216]
