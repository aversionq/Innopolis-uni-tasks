def is_repeating_digits(number : int) -> bool:
    return not len(set(str(number))) == len(list(str(number)))


user_input = int(input())
if is_repeating_digits(user_input):
    print("YES")
else:
    print("NO")
