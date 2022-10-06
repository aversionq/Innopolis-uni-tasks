def is_string_intersection(str1 : str, str2 : str) -> bool:
    str1_dict = dict.fromkeys(set(str1), 0)
    str2_dict = dict.fromkeys(set(str2), 0)
    for letter in str1:
        str1_dict[letter] += 1
    for letter in str2:
        str2_dict[letter] += 1
    
    if set(str1).intersection(set(str2)) == set(str2):
        for i in str2:
            if str1_dict[i] < str2_dict[i]:
                return False    
        return True
    
    return False


user_input1 = input()
user_input2 = input()
print(is_string_intersection(user_input1, user_input2))
