def remove_different_digits(array):
    new_arr = []
    for num in array:
        if len(set(str(abs(num)))) != len(str(abs(num))):
            new_arr.append(num)
    
    return new_arr


amount = int(input())
numbers = list(map(int, input().split()))
changed_arr = remove_different_digits(numbers)
for i in range(len(changed_arr)):
    print(changed_arr[i], end=" ")
