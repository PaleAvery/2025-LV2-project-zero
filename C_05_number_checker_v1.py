# functions go here
def num_check(question, num_type, exit_code=None):
    """Checks that users enter an integer or float that is more than
    zero (or the optional exit code)"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter an integer more than zero."
        change_to = int

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that its more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here

# loops for testing purposes
while True:
    print()

    my_float = num_check("please enter a number more than 0: ", "float")
    print(f"Thanks.  You chose {my_float}")
    print()
    my_int = num_check("please enter an integer more than 0",
                         "integer", "")
    if my_int == "":
        print("you have chosen infinite mode")
    else:
        print(f"Thanks you chose {my_int}")
