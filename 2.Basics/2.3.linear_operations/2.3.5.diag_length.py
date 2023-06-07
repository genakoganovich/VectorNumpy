import numpy as np

ab, ad = [np.array(list(map(float, input().split()))) for _ in range(2)]
print(np.linalg.norm(ab + ad), np.linalg.norm(ab - ad))
