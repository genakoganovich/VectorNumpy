import numpy as np
# Создаем одномерные массивы
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Вычисляем векторное произведение с указанием осей
c = np.cross(a, b, axisa=0, axisb=0, axisc=0)
print("Вектор a:", a)
print("Вектор b:", b)
print("Векторное произведение a x b с указанием осей:", c)