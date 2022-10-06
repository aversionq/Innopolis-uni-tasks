def prof_by_k(arr, k : int):
    return [i * k for i in arr]

array = []
amount = int(input())
for i in range(amount):
    array.append(int(input()))
mult_by = int(input())
changed_arr = prof_by_k(array, mult_by)
for i in range(amount):
    print(changed_arr[i], end=" ")
