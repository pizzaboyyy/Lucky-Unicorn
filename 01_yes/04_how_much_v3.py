# Component 2 (how much) v3
# More effecient method - includes valid range on the basis of while loop
# which eliminates the need to use the 'valid' variable

# main routine
error = "That was not a valid input\n"
user_balance = 0

# keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    try:
        # ask for amount
        user_balance = int(input("Please enter a whole number between 1 and 10"
                                 "\nHow much do you want to play with? $"))
        print()

    except ValueError:
        print(error)

print(f"You are playing with {user_balance}")