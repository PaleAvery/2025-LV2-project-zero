# functions go here
def int_check(question, low, high):
    """checks users enter an integer between 2 values"""

    error = f"oops - please enter an integer between {low} and {high}."



    while True:
        response = input(question).lower()

        # check for the exit code
        if response == "xxx":
            return response

        try:
            # Change the response to an integer and check that its more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here

# loops for testing purposes
while True:
    print()

    # ask user for an integer
    my_num = int_check("choose a number: ", 1, 10 )
    print(f"you chose {my_num}")
