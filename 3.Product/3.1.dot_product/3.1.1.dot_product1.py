import numpy as np

a, b = [np.array(input().split()).astype(float) for i in range(2)]
print(a @ b)