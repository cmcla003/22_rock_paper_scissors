# Functions go here
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

# Main routine goes here
# set up rock/paper/scissors list
rps_list = ["rock","paper","scissors","exit"]

user_choice = ""
while user_choice != "exit":
    # ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors: ",rps_list,
                                 "Please enter rock / paper / scissors or exit to quit." )

    # print out choice for comparison purposes.
    print("You chose {}".format(user_choice))