import numpy as np

# Создаем вектор
v = np.array([3, -1, 4])

# Вычисляем L1-норму вектора
norm_l1 = np.linalg.norm(v, ord=1)

print(norm_l1)  # 8.0
