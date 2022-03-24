# set up variables
rounds_played = 0
rounds_lost = 0
rounds_draw = 0

# test list data
test_results = ["Win", "Win", "Loss", "Loss", "Draw"]

for item in test_results:
    rounds_played += 1

    result = item

    if result == "Draw":
        result = "It's a draw"
        rounds_draw +=1
    elif result == "Loss":
        result = "You Lose."
        rounds_lost += 1

# calcualte numbers of win
rounds_won = rounds_played - rounds_lost - rounds_draw

# Output results
print()
print("**** End Game Summary ***")
print("Won: {} \t | \t Lost: {} \t | \t Draw: {}".format(rounds_won,rounds_lost,rounds_draw))

