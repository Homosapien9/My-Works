def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    average = card_average(hand)
    return ((hand[0] + hand[-1]) / 2 == average or hand[len(hand) // 2] == average)

def average_even_is_average_odd(hand):
    even_average = sum(hand[0::2]) / len(hand[0::2])
    odd_average = sum(hand[1::2]) / len(hand[1::2])
    return even_average == odd_average
    
def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
