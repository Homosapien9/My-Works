def get_rounds(number):
    return [number,number+1,number+2]

def concatenate_rounds(rounds_1, rounds_2):
    list= rounds_1
    for i in rounds_2:
        list.append(i)
    return list
    
def list_contains_round(rounds, number):
    if number in rounds:
        return True
    else:
        return False
        
def card_average(hand):
    avg = sum(hand)/len(hand)
    return avg

def approx_average_is_average(hand):
    if (hand[0]+hand[-1])/2 == card_average(hand) or hand[len(hand)//2]==card_average(hand):
        return True
    else:
        return False
def average_even_is_average_odd(hand):
    if [sum(hand[0::2])/len(hand[0::2])]==[sum(hand[1::2])/len(hand[1::2])]:
        return True
    else :
        return False

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
