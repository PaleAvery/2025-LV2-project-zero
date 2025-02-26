import pandas


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

        response = input(question)

        # check for exit code and return it if entered
        if response == exit_code:
            return response
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
    all_amounts = []
    all_dollar_per_item = []

    # expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    # loop to get expenses
    amount = 1
    while True:
        item_name = not_blank("item name: ")

        # check users enter at least one variable expense
        if (exp_type == "variable" and item_name == "xxx") \
                and len(all_items) == 0:
            print(" oops you have not entered anything "
                  "you need at least one item")
            continue

        elif item_name == "xxx":
            break

        amount = num_check(f"How many <enter for {how_many}>: ",
                           "integer", "")

        if amount == "":
            amount = how_many

        cost = num_check("price for one", "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_costs.append(cost)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate row cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    subtotal = expense_frame['Cost'].sum()

    # returns all items for now so we can check loop
    return expense_frame, subtotal


# main routine starts here

quantity_made = num_check("quantity being made: ",
                          "integer")
print()

print("getting variable costs ...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print(variable_expenses)
print(variable_subtotal)
