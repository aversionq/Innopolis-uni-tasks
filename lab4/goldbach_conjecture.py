def is_prime(num : int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def goldbach_conjecture(num_sum : int) -> str:
    for i in range(2, num_sum):
        if is_prime(i):
            for j in range(i, num_sum):
                if is_prime(j):
                    if num_sum == (i + j):
                        prime_arr = sorted([i, j])
                        return f"{prime_arr[0]} {prime_arr[1]}"


user_input = int(input())
print(goldbach_conjecture(user_input))
