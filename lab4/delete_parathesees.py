def remove_parentheses_content(text : str) -> str:
    count_par = min(text.count("("), text.count(")"))
    for i in range(count_par):
        par_ind_begin = text.find("(")
        par_ind_end = text.find(")")
        text = text[:par_ind_begin] + text[par_ind_end + 1:]
    return text

amount = int(input())
str_list = []
for i in range(amount):
    str_list.append(input())
    str_list[i] = remove_parentheses_content(str_list[i])

for i in range(amount):
    print(str_list[i])
