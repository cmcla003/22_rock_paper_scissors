
# list to pull choices from without extis for testing
rps_list = ["rock","paper","scissors"]

# loop for testing
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # compare options
        if user_choice == comp_choice:
            result="Draw"
        elif user_choice == "rock" and comp_choice == "scissors":
            result="Win"
        elif user_choice == "paper" and comp_choice == "rock":
            result = "Win"
        elif user_choice == "scissors" and comp_choice == "paper":
            result="Win"
        else:
            result="You lose"

        print("You chose {}, Computer chose {}. "
              "\n Result: {}".format(user_choice,comp_choice,result))

    comp_index += 1
    print()
