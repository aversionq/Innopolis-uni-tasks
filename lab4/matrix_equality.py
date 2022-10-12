def replace_evens_by_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = 0


def is_matrix_equal(f_matrix, s_matrix):
    for i in range(len(f_matrix)):
        if not (f_matrix[i] == s_matrix[i]):
            return False
    return True


m_size = list(map(int, input().split()))
first_matrix = []
second_matrix = []
for i in range(m_size[0]):
    row = list(map(int, input().split()))
    first_matrix.append(row)
for i in range(m_size[0]):
    row = list(map(int, input().split()))
    second_matrix.append(row)

replace_evens_by_zero(first_matrix)
replace_evens_by_zero(second_matrix)

if is_matrix_equal(first_matrix, second_matrix):
    print("YES")
else:
    print("NO")
