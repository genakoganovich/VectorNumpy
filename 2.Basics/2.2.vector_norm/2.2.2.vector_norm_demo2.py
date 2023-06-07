import numpy as np

# Создаем двумерный массив
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Вычисляем модуль каждой строки матрицы
norm_rows = np.linalg.norm(A, axis=1)

print(norm_rows)  # [ 3.74165739  8.77496439 13.92838828]

print(np.linalg.norm(np.array([1, 2, 3])))
print(np.linalg.norm(np.array([4, 5, 6])))
print(np.linalg.norm(np.array([7, 8, 9])))
