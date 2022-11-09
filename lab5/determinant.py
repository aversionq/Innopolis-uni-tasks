import numpy as np


amount = int(input())
matrix = []
for i in range(amount):
    matrix.append(list(map(float, input().split())))

np_matrix = np.array(matrix)
determinant = np.linalg.det(np_matrix)
print(f"{determinant:.8f}")
