import numpy as np


matrix = []
amount = int(input())
for i in range(amount):
    matrix.append(list(map(int, input().split())))

np_matrix = np.array(matrix)
secondary_diag = np.fliplr(np_matrix).diagonal()
for i in range(amount):
    print(secondary_diag[i], end=" ")
