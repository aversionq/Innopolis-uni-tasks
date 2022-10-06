def find_some_sum(arr, k, m):
    result = 0
    for i in range(len(arr)):
        if (abs(arr[i]) % 10 == k and abs(arr[i]) % m != 0):
            result += arr[i]
    
    return result

start_info = list(map(int, input().split(" ")))
numbers = list(map(int, input().split(" ")))
print(find_some_sum(numbers, start_info[2], start_info[1]))
