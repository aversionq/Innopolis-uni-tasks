import numpy as np


amount = int(input())
matrix = []
for i in range(amount):
    matrix.append(list(map(float, input().split())))

np_matrix = np.array(matrix)
inv_matrix = np.linalg.inv(np_matrix)
for i in range(amount):
    for j in range(amount):
        print(f"{inv_matrix[i][j]:.8f}", end=" ")
    print()
