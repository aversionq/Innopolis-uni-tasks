def is_prime(number : int) -> bool:
    for i in range(2, int(number ** 0.5) + 1):
        if not (number % i):
            return False
    return True

number_to_check = int(input("Input number: "))
if is_prime(number_to_check):
    print("Yes")
else:
    print("No")
