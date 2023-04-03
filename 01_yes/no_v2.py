# LU Yes / NO
# simplifies the input by converting it to lower case. also , accepts y or n async abbreviations.
# Prints result of user choice as well as input - for testing


# Ask the user if they have playeed before
show_instructions = input("Have you played this game before?: ").lower()
# If they say yes, output 'Program Continues
if show_instructions == "yes" or show_instructions == "y":
    print("Program continues")

# If they say no, output 'display instructions'
elif show_instructions == "no" or show_instructions == "no":
    print("Display instructions")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no'")