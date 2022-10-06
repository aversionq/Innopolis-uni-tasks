def get_name_of_card(suit : int, num : int) -> str:
    suits = {
        1 : "spades",
        2 : "clubs",
        3 : "diamonds",
        4 : "hearts"
    }
    quals = {
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "jack",
        12 : "queen",
        13 : "king",
        14 : "ace"
    }

    return f"the {quals[num]} of {suits[suit]}"


user_input = list(map(int, input().split()))
print(get_name_of_card(user_input[0], user_input[1]))
