# functions go here
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


#main routine goes here
#payment_ans = ['cash', 'credit']
while True:
    want_instructions = string_check("do you want to see the instructions? ")
    print(f"you chose {want_instructions}")
    print()
#pay_method = string_check("Payment method:", payment_ans, 2)
#print(f"you chose {pay_method}")