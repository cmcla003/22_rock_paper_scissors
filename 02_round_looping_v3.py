# Function to check input is valid

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


# *** Main Routine ***

rounds_played = 0
choose_instruction = "Please choose Rock/Paper/Scissors"

rounds=check_rounds("How many rounds? ", "Please type either <enter> for continuous mode "
                    "or and integer more than 0")

end_game = "no"
while end_game == "no":

    # round heading
    if rounds == "":
        heading = "Continous Mode: Round {}".format(rounds_played+1)
    else:
        heading = " Round {} of {}".format(rounds_played+1, rounds)

    print(heading)
    choose = input("{} or exit to end: ".format(choose_instruction))

    if choose == "exit":
        break


    if rounds_played == rounds -1:
        end_game = "yes"

    print(heading)
    print("You chose : {}".format(choose))
    rounds_played +=1

print("Thanks for playing")
