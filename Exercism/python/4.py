def exchange_money(budget, exchange_rate):
    return float(float(budget)/float(exchange_rate))

def get_change(budget, exchanging_value):
    return float(float(budget)-float(exchanging_value))

def get_value_of_bills(denomination, number_of_bills):
    return int((denomination)*(number_of_bills))

def get_number_of_bills(amount, denomination):
    return int(amount//denomination)

def get_leftover_of_bills(amount, denomination):
    return float((amount)%(denomination))

def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_rate = exchange_rate * (1 + spread / 100)
    exchanged = budget / actual_rate
    return int(exchanged // denomination * denomination)
