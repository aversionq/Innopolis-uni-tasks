def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]


user_input = list(map(int, input().split()))
rows = user_input[0]
columns = user_input[1]
m = []
for i in range(rows):
    row = list(map(int, input().split()))
    m.append(row)

m = transpose(m)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=" ")
    print()
