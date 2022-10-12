def matrix_prod(matrix, dub_matrix):
    length = len(matrix) 
    result_matrix = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result_matrix[i][j] += matrix[i][k] * dub_matrix[k][j]
    return result_matrix

matrix = []
m_size = int(input())
for i in range(m_size):
    row = list(map(float, input().split()))
    matrix.append(row)

matrix_tmp = matrix.copy()

for i in range(m_size - 1):
    matrix = matrix_prod(matrix, matrix_tmp)

for i in range(m_size):
    for j in range(m_size):
        print("{:.3f}".format(matrix[i][j]), end=" ")
    print()
