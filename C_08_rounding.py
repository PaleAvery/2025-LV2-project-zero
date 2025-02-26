import math


# rounding function
def round_up(amount, round_val):
    """rounds amount to desired hole number"""
    return int(math.ceil(amount / round_val)) * round_val


# main routine here

# loop for testing purposes
while True:
    quantity_made = int(input(" # of items"))
    total_expenses = float(input("total expenses"))
    target = float(input("profit goal"))
    round_to = int(input("round to"))

    selling_price = (total_expenses + target) / quantity_made
    suggested_price = round_up(selling_price, round_to)

    print(f"Minimum price: ${selling_price:.2f}")
    print(f"suggested price: ${suggested_price:.2f}")
    print()

