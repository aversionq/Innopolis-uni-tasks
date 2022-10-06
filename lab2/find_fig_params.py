import math as m


def count_parameters(*args):
    if len(args[0]) == 2:
        radius = float(args[0][1])
        perimeter = m.pi * 2 * radius
        square = m.pi * radius ** 2
    elif len(args[0]) == 3:
        side1 = float(args[0][1])
        side2 = float(args[0][2])
        perimeter = (side1 + side2) * 2
        square = side1 * side2
    else:
        side1 = float(args[0][1])
        side2 = float(args[0][2])
        side3 = float(args[0][3])
        perimeter = side1 + side2 + side3
        half_p = perimeter / 2
        square = m.sqrt(half_p * (half_p - side1) * (half_p - side2) * (half_p - side3))
    
    return perimeter, square

info = input().split(" ")
perim, sq = count_parameters(info)
print("{:.4f} {:.4f}".format(perim, sq))
