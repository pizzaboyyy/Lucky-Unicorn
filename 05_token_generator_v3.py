# component 3 (random tokens v3)
# format currency
# ensure odds favour the house - has a 10% chance of a unicorn and a 30% for the zebra, donkey and horse
import random

tokens = ["unicorn"
          "horse","horse","horse"
          "zebra", "zebra", "zebra"
          "donkey", "donkey", "donkey"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE


# testing loop to generate 100 tokens
for item in range(500):
    token = random.choice(tokens)

    # Adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= -1
    else:
        balance -= .50

    # output
print(f"Starting Balance = ${STARTING_BALANCE:.2f}")
print(f"Final Balance = ${balance:.2f}")

