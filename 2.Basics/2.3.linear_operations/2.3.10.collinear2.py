import numpy as np

a, b = [np.array(input().split()).astype(float) for i in range(2)]
print([False, True][len(np.unique(a/b)) == 1])
