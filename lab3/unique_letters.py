def get_unique_letters(text : str) -> str:
    letter_dict = dict.fromkeys(set(text), 0)
    for letter in text:
        letter_dict[letter] += 1
    
    arr = []
    for key in set(text):
        if letter_dict[key] == 1:
            arr.append(key)
    
    return "".join(sorted(arr))


user_input = input()
print(get_unique_letters(user_input))
