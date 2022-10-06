def remove_extra_spaces(text : str) -> str:
    splitted_text = list(filter(None, text.split(" ")))
    for i in range(len(splitted_text)):
        splitted_text[i] = splitted_text[i].strip()
    return " ".join(splitted_text)

print(remove_extra_spaces(input()))
