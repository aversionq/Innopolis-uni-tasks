def fibonacci_k(num : int) -> int:
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci_k(num - 1) + fibonacci_k(num - 2)


user_input = int(input())
print(fibonacci_k(user_input))
