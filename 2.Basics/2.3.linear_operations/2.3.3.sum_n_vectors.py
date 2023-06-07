import numpy as np

n = int(input())
sum_result = np.zeros(3)
for i in range(n):
    sum_result = np.add(sum_result, np.array(list(map(float, input().split()))))

print(sum_result)
