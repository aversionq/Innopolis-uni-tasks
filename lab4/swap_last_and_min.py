def swap_last_min(arr):
    min_ind = arr.index(min(arr))
    temp = min(arr)
    arr[min_ind] = arr[len(arr) - 1]
    arr[len(arr) - 1] = temp
    return arr


user_input = list(map(int, input().split()))
rows = user_input[0]
columns = user_input[1]
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split())))

ch_arr = []
for i in range(columns):
    for j in range(rows):
        ch_arr.append(matrix[j][i])
    ch_arr = swap_last_min(ch_arr)

    for j in range(rows):
        matrix[j][i] = ch_arr[j]
    ch_arr.clear()

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
