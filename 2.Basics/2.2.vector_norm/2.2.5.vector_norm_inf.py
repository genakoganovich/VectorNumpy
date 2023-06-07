import numpy as np

# Создаем вектор
v = np.array([3, -1, 4])

# Вычисляем L-бесконечность норму вектора
norm_inf = np.linalg.norm(v, ord=np.inf)

print(norm_inf)  # 4.0
