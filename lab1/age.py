def print_age(age : int) -> str:
    if age % 10 == 1 and (12 < age < 110 or age < 10):
        return f"Мне {age} год"
    elif age % 10 in [2, 3, 4]:
        if 10 > age or 14 < age < 110:
            return f"Мне {age} года"
        return f"Мне {age} лет"
    return f"Мне {age} лет"

print(print_age(int(input("Input age: "))))

for i in range(121):
    print(print_age(i))