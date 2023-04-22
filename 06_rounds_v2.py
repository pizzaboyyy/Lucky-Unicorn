# Component 4 - game mechanics and looping v2
# based on 06_rounds_v1
# removed hard-wiring so that all tokens can be allocated (randit 1-100)
# gives user feedback about number of rounds and maintains balance
# test amount set to $5


import random

# main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# Testing loop to generated 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds
    number = random.randint(1, 100)  # can only be a donkey

    # adjust balance
    # if the random number is between 1 and 5
    # user gets a unicorn (adds $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    # If the random number is between 6 and 36
    # user gets a donkey -$1
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    # in all the other cases the token must be a horse or a zebra
    # (subtract 0.50 from balance in both cases)
    else:
        # if the number is even set the token to zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5
        # Otherwise set the token to horse
        else:
            token = "horse"
            balance -= .5

    # output
    print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
    if balance < 1:
        print("\n Sorry but you ran out of money")
        play_again = "x"
    else:
        play_again = input("\n Do you want to play another round \n <enter> to play "
                           "again or 'x' to exit: ").lower()
        print()

print("Thanks for playing")
print(f"You started with ${TEST_AMOUNT:.2f}")
print(f"and leave with ${balance:.2f}")
print("Goodbye")




