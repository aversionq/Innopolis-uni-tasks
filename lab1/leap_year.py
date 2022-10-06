def leap_year_days(year_number):
    if not (year_number % 4) and year_number % 100 or not (year_number % 400):
        return 29
    else:
        return 28

print(leap_year_days(int(input("Input year number: "))))
