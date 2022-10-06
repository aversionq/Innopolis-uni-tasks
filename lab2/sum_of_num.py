def sum_of_digits(text : str) -> int:
    result = 0
    for i in range(len(text)):
        if text[i].isdigit():
            result += int(text[i])
    
    return result

print(sum_of_digits(input()))
