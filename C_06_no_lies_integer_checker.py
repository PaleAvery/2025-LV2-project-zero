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



# main routine goes here

# loop for testing purposes
while True:
    print()

    #ask user for their name
    name = input("name: ") # replace with call to 'not blank' fucntion

    # Ask user for their age and check if its between 12 and 120
    age = int_check("Age: ")

    #output error message / success message
    if age <12:
        print(f"{name} is to young")
        continue
    elif age > 120:
        print(f"{name} is to old")
        continue
    else:
        print(f"{name} bought a ticket")

    # ask user for an integer
  #  my_num = int_check("Choose a number more than zero:")
   # print(f"You chose {my_num}")

