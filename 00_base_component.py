import random

# Functions go here
# Choice checker assesses valid input
def choice_checker(question,valid_list,error):

    valid = False
    while not valid:
        # Ask user for choice
        response = input(question).lower().strip()

        for item in valid_list:
            if response == item[0] or response == item:
                return response

        print(error)
        print()


# **** Main Routine ***
# Lists / Initalised variables go here
yes_no_list = ["yes", "no"]
rps_list = ["rock","paper","scissors","exit"]

# Ask user if played before

# If no show instructions

# Ask user fro number of round then loop ...

# Ask user is they want to see their game history
# If yes show history

# Show game statistics