# Function to check input is valid

def check_rounds():
    while True:
        response = input("How many rounds? ")

        round_error = "Please type either <enter> or and integer more than 0"

        if response != "":
            try:
                response= int(response)

                if response <1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# *** Main Routine ***

rounds_played = 0
choose_instruction = " Please choose Rock/Paper/Scissors"

rounds=check_rounds()

end_game = "no"
while end_game == "no":

    # round heading
    if rounds == "":
        heading = "Continous Mode: Round {}".format(rounds_played+1)
        print(heading)
        choose = input("{} or exit to end".format(choose_instruction))
        if choose == "exit":
            break
    else:
        heading = " Round {} of {}".format(rounds_played+1, rounds)
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds -1:
            end_game = "yes"

    print("You chose : {}".format(choose))
    rounds_played +=1

print("Thanks for playing")