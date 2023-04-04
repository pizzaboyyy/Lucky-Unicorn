# took function from compnent 03_v1 as the basis for this new function which
# incorparates both yes/no and show instructions


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have playeed before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


        print(f"You entered '{answer}'")

# function to display instructions
def instructions():
    print("***** How to play ******")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# Main routine go here...
played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    instructions()
else:
    print("Program continues")

