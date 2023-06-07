import numpy as np

norm, angle = [float(input()) for i in range(2)]
print(round(norm * np.cos(angle), 2), round(norm * np.sin(angle), 2))

