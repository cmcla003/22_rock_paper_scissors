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
summary_stats = []
rounds_played = 0
rounds_lost = 0
rounds_draw = 0
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
        heading = "Round {} of {}".format(rounds_played+1, rounds)
        if rounds_played == rounds - 1:
            end_game = "yes"

    print(heading)
    # ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (or exit to quit): ", rps_list,
                                 "Please enter rock / paper / scissors or exit to quit.")

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # compare user choice with computer choice
    if user_choice == comp_choice[0]:
        result = "Draw"
        rounds_draw += 1
    elif user_choice == "rock" or user_choice =="r" and comp_choice == "scissors":
        result = "Win"
    elif user_choice == "paper" or user_choice =="p" and comp_choice == "rock":
        result = "Win"
    elif user_choice == "scissors" or user_choice =="s" and comp_choice == "paper":
        result = "Win"
    # exit code to end program early / if in continuous mode
    elif user_choice == "exit":
        break
    else:
        result = "You lose"
        rounds_lost += 1

    print("You chose {}, Computer chose {}. "
          "\nResult: {}".format(user_choice, comp_choice, result))

    summary_stats.append(result)



    print(heading)
    print()
    rounds_played +=1

    # calculate numbers of win
    rounds_won = rounds_played - rounds_lost - rounds_draw

# calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_draw = rounds_draw / rounds_played * 100

print("Thanks for playing")

# Ask user is they want to see their game history
# If yes show history
print()
print("*** Game History ***")
for game in summary_stats:
    print(game)

# Show game statistics
print()
print(" *** Game Statistics ***")
print("Win:{} | {:.0f}% \nLoss:{} | {:.0f}% \nDraw:{} | {:.0f}%"
      .format(rounds_won,percent_win,rounds_lost,percent_lose,rounds_draw,percent_draw))