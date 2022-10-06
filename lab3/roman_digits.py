def roman_to_arabic(roman_digit : str) -> int:
    roman_arabic_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    if roman_digit in list(roman_arabic_dict.keys()):
        return roman_arabic_dict[roman_digit]
    else:
        return 0


user_input = input()
print(roman_to_arabic(user_input))
