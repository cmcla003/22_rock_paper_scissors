summary_stats = []

rounds_played = 0
rounds_lost = 0
rounds_draw = 0

for item in range (0,5):
    result = input("Choose result: ")
    rounds_played += 1

    outcome = "Round {}:{}".format(item, result)

    if result == "lost":
        rounds_lost += 1
    elif result == "draw":
        rounds_draw += 1

    summary_stats.append(outcome)

    # calculate numbers of win
    rounds_won = rounds_played - rounds_lost - rounds_draw

# calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_draw = rounds_draw / rounds_played * 100

print()
print("*** Game History ***")
for game in summary_stats:
    print(game)

# Game statistics
print()
print(" *** Game Statistics ***")
print("Win:{} | {:.0f}% \nLoss:{} | {:.0f}% \nDraw:{} | {:.0f}%"
      .format(rounds_won,percent_win,rounds_lost,percent_lose,rounds_draw,percent_draw))