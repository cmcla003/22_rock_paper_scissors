summary_stats = []

for item in range (1,6):
    choice = input("Round {}: ".format(item))
    summary_stats.append(choice)

print()
print("*** Summary Statistics ***")
for item in summary_stats:
    print(item)