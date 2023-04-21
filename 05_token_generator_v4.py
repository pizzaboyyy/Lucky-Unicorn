# component 3 (random tokens v4)
# Calculate percentage to ensure the odds favour the house
# 5% unicorns 30% donkeys and the remaining 65% horses/zebras
import random


STARTING_BALANCE = 100
balance = STARTING_BALANCE


# testing loop to generate 100 tokens
for item in range(10):
    number = random.randint(1, 100)

    # Adjust balance
    # If the number is between 1 and 5
    # user gets a unicorn (adds $4 to the balance)
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
    print(f"Token: {token}, Balance: {balance:.2f}")

print()
print(f"Starting Balance = ${STARTING_BALANCE:.2f}")
print(f"Final Balance = ${balance:.2f}")

