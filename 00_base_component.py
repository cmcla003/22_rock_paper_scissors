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

# Number check for rounds (integer only error for everything else)
def check_rounds(question, error):
    while True:
        response = input(question)

        if response != "":
            try:
                response= int(response)

                if response <1:
                    print(error)
                    continue

            except ValueError:
                print(error)
                continue

        return response

# **** Main Routine ***
# Lists / Initalised variables go here
yes_no_list = ["yes", "no"]
rps_list = ["rock","paper","scissors","exit"]
rounds_played = 0
# Ask user if played before

# If no show instructions

# Ask user for number of round then loop ...
rounds=check_rounds("How many rounds? ", "Please type either <enter> for continuous mode "
                    "or and integer more than 0")

end_game = "no"
while end_game == "no":

    # round heading
    if rounds == "":
        heading = "Continous Mode: Round {}".format(rounds_played+1)
    else:
        heading = " Round {} of {}".format(rounds_played+1, rounds)
        if rounds_played == rounds - 1:
            end_game = "yes"

    print(heading)
    # ask user for choice and check it's valid
    choose = choice_checker("Choose rock / paper / scissors (or exit to quit): ", rps_list,
                                 "Please enter rock / paper / scissors or exit to quit.")

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Computer Choice:",comp_choice)

    if choose == "exit":
        break


    print(heading)
    print("You chose : {}".format(choose))
    print()
    rounds_played +=1

print("Thanks for playing")

# Ask user is they want to see their game history
# If yes show history

# Show game statistics