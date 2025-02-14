# functions go here
def int_check(question):
    """Checks users enter an integer that is more than zero (or the 'xxx' exit code)"""

    error = "oops - please enter an integer."

    while True:

        try:
            response = int(input(question))

            return response

        except ValueError:
            print(error)



def not_blank(question):
    """Checks that a user response is not blank """

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this cant be blank. Please try again.\n")


def string_check(question, valid_answers=('yes','no'),
                 num_letters=1):
    """Checks the users enter the full word
    or the 'n' letter/s of a worf from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if its the first letter
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")


# main routine goes here

# initialise variables / non default options for string checker
payment_ans = ('cash','credit')
# Ticket Price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# loop for testing purposes
while True:
    print()

    # ask user for their name and check its not blank
    name = not_blank("Name: ")

    # ask user for their age and check its between 12 and 120
    age = int_check("Age: ")

    # Output error message and success message
    if 12 <= age < 16:
        ticket_price = CHILD_PRICE

    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE
    elif 65 <= age <121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is to old")
        continue

    # ask user for payment method (cash credit ca and ar)
    pay_method = string_check("Payment method: ", payment_ans,2)

    if pay_method == "cash":
        surcharge = 0

    # if someone is paying by credit calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # calculate total payable
    total_to_pay = ticket_price +surcharge

    print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f" the total payable is ${total_to_pay:.2f}\n")
    #print(f"{name} has bought a ticket ({pay_method}) ")




