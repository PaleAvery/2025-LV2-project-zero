# functions go here
def string_check(question, valid_ans_list, num_letters):
    """Checks the users enter the full word
    or the 'n' letter/s of a worf from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if its the first letter
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_ans_list}")


#main routine goes here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check("do you like coffee? ",
                           yes_no_list, 1)
pay_method = string_check("Payment method:", payment_list, 2)
print(f"you chose {pay_method}")