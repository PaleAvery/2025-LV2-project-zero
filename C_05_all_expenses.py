import pandas
from tabulate import tabulate
from datetime import date


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


def get_expenses(exp_type, how_many=1):
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

    # defualt for fixed expenses
    amount = how_many
    how_much_question = "How much? $"

    # loop to get expenses
    while True:
        item_name = not_blank("item name: ")

        # check users enter at least one variable expense
        if (exp_type == "variable" and item_name == "xxx") and len(all_items) == 0:
            print(" oops you have not entered anything "
                  "you need at least one item")
            continue

        elif item_name == "xxx":
            break

        if exp_type == "variable":

            amount = num_check(f"How many <enter for {how_many}>: ",
                               "integer", "")

            if amount == "":
                amount = how_many

            how_much_question = "price for one? $"

        # get price for item question customized depending on expense type
        price_for_one = num_check(how_much_question, "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate row cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']
    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # apply currency formating
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)
    # returns all items for now so we can check loop
    # make expense frame into a string with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys',
                                  tablefmt='psql', showindex=False)

    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys',
                                  tablefmt='psql', showindex=False)

    return expense_string, subtotal


def currency(x):
    return "${:.2f}".format(x)


# main routine starts here

quantity_made = num_check("quantity being made: ",
                          "integer")
print()

print("getting variable costs ...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print("getting fixed costs...")
fixed_expenses = get_expenses("fixed")
print()
fixed_panda = fixed_expenses[0]
fixed_subtotal = fixed_expenses[1]

# temperary putput area

print("=== variable expenses ===")
print(variable_panda)
print(f"variable subtotal: ${variable_subtotal:.2f}")
print()

print("=== fixed expenses ===")
print(fixed_panda)
print(f" fixed subtotal ${variable_subtotal:.2f}")

print()
total_expenses = variable_subtotal + fixed_subtotal
print(f"Total Expenses ${total_expenses:.2f}")
print(variable_expenses)
print(variable_subtotal)
