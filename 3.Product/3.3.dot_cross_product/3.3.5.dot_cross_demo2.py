import numpy as np
# Векторы A, B и C
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])
# Вычисление первого векторного произведения
cross_product_1 = np.cross(B, C)
# Вычисление второго векторного произведения
double_cross_product = np.cross(A, cross_product_1)
# Вывод результата
print("Двойное векторное произведение: ", double_cross_product)
