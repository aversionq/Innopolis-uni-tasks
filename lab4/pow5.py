def is_pow_of_five(num : int) -> bool:
    for i in range(13):
        if 5 ** i == num:
            return True
    return False

amount = int(input())
numbers = list(map(int, input().split()))
counter = 0
for num in numbers:
    if is_pow_of_five(num):
        counter += 1

print(counter)