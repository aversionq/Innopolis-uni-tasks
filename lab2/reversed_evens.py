def reverse_even_chars(text : str) -> str:
    return "".join([text[i] for i in range(1, len(text), 2)])[::-1]

print(reverse_even_chars(input()))
