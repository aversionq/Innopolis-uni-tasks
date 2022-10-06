def count_days_by_leaves(leaves_start, leaves_end):
    days_enough = 1
    days_full = 1
    leaves_check_1 = leaves_start
    leaves_check_2 = leaves_start
    while leaves_start < leaves_end:
        leaves_start *= 3
        days_enough += 1
    while leaves_check_2 < 1000000:
        leaves_check_1 *= 3
        leaves_check_2 += leaves_check_1
        days_full += 1

    return days_enough, days_full

input_vals = input()
l_st, l_end = int(input_vals.split(" ")[0]), int(input_vals.split(" ")[1])
res_1, res_2 = count_days_by_leaves(l_st, l_end)
print(f"{res_1} {res_2}")
