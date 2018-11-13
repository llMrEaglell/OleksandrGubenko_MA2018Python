# Rock-paper-scissors-lizard-Spock template
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions
print("---Rock-Paper-Scissors-Lizard-Spock Game---")

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    #0
    if name == "rock":
        return 0
    #1
    elif name=="Spock":
        return 1
    #2
    elif name=="paper":
        return 2
    #3
    elif(name=="lizard"):
        return 3
    #4
    elif(name=="scissors"):
        return 4
    #NotFound
    else:
        return "Bad, choice not found, try again"


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    # convert number to a name using if/elif/else
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "Scissors"
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print("\n")
    # print out the message for the player's choice
    print('Player choise is: {}'.format(player_choice))
    # convert the player's choice to player_number using the function name_to_number()
    player_number=name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(4)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)
    # print out the message for computer's choice
    print("Computer's choice is: {}".format(comp_choice))
    # compute difference of comp_number and player_number modulo five
    difference = ((player_number - comp_number) % 5)
    # use if/elif/else to determine winner, print winner message
    if difference== 1 or difference==3:
        print("Plауеr wins!")
    elif difference== 2 or difference== 4:
        print ("Computer Win")
    elif difference == 0:
        print("Plауеr аnd cоmputеr tiе!")
    else:
        print("Bad input data")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
