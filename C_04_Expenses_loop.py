def not_blank(question):
    """Checks that a user response is not blank """

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this cant be blank. Please try again.\n")

def num_check(question, num_type="float", exit_code=None):
    """checks that response is a float or integer more than zero"""

    if num_type == "float":
        error = "please enter a number more than zero."
    else:
        error = "please enter an integer more than zero."

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def get_expenses(exp_type):
    """ gets variable fixed expenses and outputs panda as a string and a sub total of the expenses"""

    # lists for panda
    all_items = []

    #expenses dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("item name: ")

        # check users enter at least one variable expense
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print(" oops you have not entered anything ")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

    # returns all items for now so we can check loop
    return  all_items


# main routine starts here

print("getting variable costs ...")