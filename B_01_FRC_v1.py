import pandas
from tabulate import tabulate
from datetime import date


# functions go herre
def make_statement(statement, decoration):
    """ Emphasises headings by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no_check(question):
    """Checks that users enter yes / y or no/n to a question"""
    #

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        if response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes(y) or no(n).\n")


def instructions():
    print(make_statement("instructions", "*"))

    print('''


for each ticket holder enter ...
- their name 
- their age 
- the payment method (cash/credit)


the program will record the ticket sale and calculate the
ticket cost ( and the profit)



Once you have either sold all the tickets or entered the
exit code ('xxx'), the program will display the ticket
sales information's and write the data to a text file 


it will also choose one lucky ticket holder who wins the 
draw (their ticket is free).

    ''')


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

        # check datatype is correct
        # is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type, how_many=1):
    """ gets variable fixed expenses and outputs panda as a string and a subtotal of the expenses"""

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

    # default for fixed expenses
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

        # get variable expenses item amount enter default to number

        if exp_type == "variable":

            amount = num_check(f"How many <enter for {how_many}>: ",
                               "integer", "")

            # allows user to push enter to default to number of items being made
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

    # calculate  cost column
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # apply currency formatting
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
    """formats numbers as currency"""
    return "${:.2f}".format(x)


# main routine starts here

# initialize variables

# assume we have no fixed expenses
fixed_subtotal = 0
fixed_panda_string = ""

print(make_statement("fund raising calculator", "7"))

print()
want_instructions = yes_no_check("do you want to see the instructions")
print()

if want_instructions == "yes":
    instructions()

print()

# get product details...
product_name = not_blank("product name")
quantity_made = num_check("quantity being made ", "integer")

# get variable expenses
print("lets get the variable expenses....")
variable_expenses = get_expenses("variable", quantity_made)

variable_panda_string = variable_expenses[0]
variable_subtotal = variable_expenses[1]

# ask user if they have fixed expenses and retrieve them
print()
has_fixed = yes_no_check("do you have fixed expenses?")

if has_fixed == "yes":
    fixed_expenses = get_expenses("fixed")

    fixed_panda_string = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

    # if the user has not entered any fixed expenses

    # set empty panda to "" so that it does not display
    if fixed_subtotal == 0:
        has_fixed = "no"
        fixed_panda_string = ""

total_expenses = variable_subtotal + fixed_subtotal
total_expenses_string = f"Total Expenses: ${total_expenses:.2f}"

# get profit goal here

# strings output area

# **** get current date for heading and filename
today = date.today()

# get day month and year as individual strings
day = today.strftime('%d')
month = today.strftime("%m")
year = today.strftime("%Y")

# headings strings
main_heading_string = make_statement(f"Fund Raising Calculator "
                                     f"({product_name}, {day}/{month}/{year})", "#")
quantity_string = f"Quantity being made : {quantity_made}"
variable_heading_string = make_statement("fixed expenses", "-")
variable_subtotal_string = f"Variable expenses subtotal ${variable_subtotal:.2f}"

# set up fixed strings
if has_fixed == "yes":
    fixed_heading_string = make_statement("fixed expenses", "-")
    fixed_subtotal_string = f"fixed statement subtotal; {fixed_subtotal:.2f}"

# set fixed cost strings to blank if we don't have fixed costs
else:
    fixed_heading_string = make_statement("you have no fixed expenses", "-")
    fixed_subtotal_string = "fixed expenses subtotal :$0.00 "
# set up fixed cost
to_write = [main_heading_string, quantity_string,
            "\n", variable_heading_string, variable_panda_string,
            variable_subtotal_string,
            "\n", fixed_heading_string, fixed_panda_string,
            fixed_subtotal_string, total_expenses_string]
# print area
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = f"{product_name}_{year}_{month}_{day}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
