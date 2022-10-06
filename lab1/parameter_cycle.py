def find_max_abs_index():
    amount = int(input())
    max_val = 0
    index = 0
    for i in range(amount):
        num = int(input())
        if abs(num) >= abs(max_val):
            max_val = num
            index = i
    return index + 1

print(find_max_abs_index())
