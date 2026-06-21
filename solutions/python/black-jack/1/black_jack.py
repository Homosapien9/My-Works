def value_of_card(card):
    if card == "A":
        return 1
    elif card in ["J", "Q", "K"]:
        return 10
    else:
        return int(card)

def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1
    if value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    return ((card_one == "A" and value_of_card(card_two) == 10) or (card_two == "A" and value_of_card(card_one) == 10))

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total <= 11