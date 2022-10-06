def count_unique_letters(text : str) -> int:
    return len(set(text.lower()))


user_text = input()
print(count_unique_letters(user_text))
