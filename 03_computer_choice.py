import random

# main routine

rps_list = ["rock","paper","scissors","exit"]

# testing loop to generate 20 examples
for item in range (0, 20):
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end='\t')