# Functions go here
def choice_checker(question):
    error = "Please enter rock / paper / scissors or exit to quit."

    valid = False
    while not valid:
        # Ask user for choice
        response = input(question).lower().strip()

        # rock input
        if response == "rock" or response == "r":
            return response
        # paper input
        elif response == "paper" or response == "p":
            return response
        elif response == "scissors" or response == "s":
            return response
        elif response == "exit":
            break
        else:
            print(error)

# Main routine goes here

user_choice = ""
while user_choice != "exit":
    # ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors: ")

    # print out choice for comparison purposes.
    print("You chose {}".format(user_choice))