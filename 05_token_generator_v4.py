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
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1
    else:
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5

        else:
            token = "horse"
            balance -= .5

    print(f"Token: {token}, Balance: {balance:.2f}")


    # output
print()
print(f"Starting Balance = ${STARTING_BALANCE:.2f}")
print(f"Final Balance = ${balance:.2f}")

