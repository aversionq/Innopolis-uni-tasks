import numpy as np


matrix = []
amount = int(input())
for i in range(amount):
    matrix.append(list(map(int, input().split())))

np_matrix = np.array(matrix)
column_max_elems = np_matrix.max(axis=0)
for i in range(amount):
    print(column_max_elems[i], end=" ")
