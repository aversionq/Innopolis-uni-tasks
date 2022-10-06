def add_stars(word : str) -> str:
    return "*" * len(word) + word + "*" * len(word)

print(add_stars(input()))
