import simplegui
import random
import math

print("=== Game === ---Guess the number--- ===")


# initialize global variables used in your code

num_range=100
secret_num=0
player_num=0
player_tries=7



# helper function to start and restart the game

def new_game():
    global secret_num,num_range,player_tries
    # sets a new secret number
    
    secret_num = random.randrange(0,num_range)
    
    
    # sets number of guesses based on range
    
    if num_range == 100 :
        player_tries=7
    elif num_range == 1000 :
        player_tries=10
    else:
        print("Bad range for number. Please choose the range")

   
    # alert the new user a new game has started

    print("\nA new game started, range from 0 to",num_range)
    print("You have",player_tries,"try for win")
    
    
# helper function to decrement guesses remaining

def decrement_guesses():
    global player_tries
    player_tries = player_tries - 1
    if player_tries > 0 :
        print("\nYou have", player_tries,"try for win")
    else :
        print("You Lose!!! The number was",secret_num)
        new_game()


# define event handlers for control panel

def range100():
    global num_range
    # For button [0,100) and restarts
    num_range=100
    new_game()


def range1000():
    global num_range
    # For button [0,1000) and restarts
    num_range=1000
    new_game()


def input_guess(guess):
    global secret_num,player_num
    ## Compares the user's guess to the secret answer #    
    player_num = int(guess)
    if player_num == secret_num :
        print("\nYou number was",player_num)
        print("You win!!!")
        new_game()
    elif player_num < secret_num :
        print("\nYou number was",player_num)
        print("Higher!")
    elif player_num > secret_num :
        print("\nYou number was",player_num)
        print("Lower!")
    else :
        print("Oh, something went wrong")
    decrement_guesses()


# create frame

frame = simplegui.create_frame("===Game---Guess the number---===", 200, 200)


# register event handlers for control elements

frame.add_button("Range [0, 100]", range100, 200)
frame.add_button("Range [0, 1000]", range1000, 200)
frame.add_input("Enter number", input_guess, 50)


# call new_game and start frame

new_game()
frame.start()
