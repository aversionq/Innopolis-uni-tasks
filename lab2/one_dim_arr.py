def change_max_sign(array):
    array[array.index(max(array))] = max(array) * (-1)

amount = int(input())
numbers = list(map(int, input().split(" ")))
change_max_sign(numbers)
for i in range(amount):
    print(numbers[i], end=" ")
