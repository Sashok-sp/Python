# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # pass
    num = 6
    if name == 'rock':
        num = 0;
    elif name == 'Spock':
        num = 1;
    elif name == 'paper':
        num = 2;
    elif name == 'lizard':
        num = 3;
    elif name == 'scissors':
        num = 4;
    else:
        num = 'Put correct name'
    return num
        
        

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    # pass
    name = ''
    if number == 0:
        name = 'rock';
    elif number == 1:
        name = 'Spock';
    elif number == 2:
        name = 'paper';
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        name = "Put correct number"
    return name
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    # pass
    
    # print a blank line to separate consecutive games
        # print ''
    # print out the message for the player's choice
        print 'Player chooses ', player_choice
    # convert the player's choice to player_number using the function name_to_number()
        player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
        comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
        comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
        print 'Computer chooses ', comp_choice
    # compute difference of comp_number and player_number modulo five
        winner = abs((comp_number - player_number) % 5)
    # use if/elif/else to determine winner, print winner message
        if winner == 0:
            print "Player and computer tie!"
            print ''
        elif winner <= 2:
            print "Computer wins!"
            print ''
        else:
            print "Player wins!"
            print ''
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
choise = raw_input("Your choise:")
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls(choise)

# always remember to check your completed program against the grading rubric


