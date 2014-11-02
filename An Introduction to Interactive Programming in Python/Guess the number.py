# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global end_range
    global count
    
    if end_range == 1000:
        count = 10
    else:
        count = 7
        
    secret_number = random.randrange(0, end_range)
    
    print 'New game. Range is from 0 to', end_range
    print 'Number of remaining guesses is', count
    print
    
   


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global end_range
    
    end_range = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global end_range
    
    end_range = 1000
    new_game()
    
    
def input_guess(guess):
    global count
    global secret_number
    
    num_guess = int(guess)
    print 'Guess was', guess
    
    count -= 1
    print 'Number of remaining guesses is', count
    
    # main game logic goes here 
    
    if count == 0 and not(secret_number == num_guess):
        print 'You run out of guesses. The number was', secret_number
        print
        new_game()
    else:
        if secret_number > num_guess:
            print 'Higher!'
            print
        elif secret_number < num_guess:
            print 'Lower!'
            print
        else:
            print 'Correct!!!'
            print
            new_game()
        
    return

    
# create frame

frame = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements and start frame

imp = frame.add_input('Guess', input_guess, 100)
but100 = frame.add_button('Range 0 - 100', range100)
but1000 = frame.add_button('Range 0- 1000', range1000)


# call new_game 

range100()


# always remember to check your completed program against the grading rubric
