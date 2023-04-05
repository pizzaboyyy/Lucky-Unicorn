# Component 2 (how much) v4
# changing v3 into a function
# also needed to change user_balance to the more generic variable name 'responce'
# and to change the condition and position of the number comparison into the loop
# to make the function recyclable


def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine
user_balance = num_check("How much would you like to pay within $", 1, 10)
print(f"You are paying with {user_balance}")


