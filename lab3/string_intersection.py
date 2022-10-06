def is_intersection(str1 : str, str2: str) -> bool:
    return set(str1).intersection(set(str2)) == set(str2)


str1 = input()
str2 = input()
print(is_intersection(str1, str2))
