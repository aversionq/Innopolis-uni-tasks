def prod_until_negative():
    num = float(input())
    result = 1
    while num >= 0:
        result *= num
        num = float(input())
    return result

print("{:.6f}".format(prod_until_negative()))
