"""
hiLo_Game.py
Programmer: Drayzdin Thompson
A random number guessing game, from one to one hundred you have ten tries to guess the number
"""
import random

def hiLo():
    '''Creates an integer from 1 to 100 that you must guess within 10 tries'''
    ans = random.randint(1,100) # Random Number Generator
    try_left = 10 # used for text, tells you how many tries are left
    loop = False # Runs game till you win
    print("I am thinking of a number from 1 to 100, can you guess what it is") # Instructions
    guess = int(input()) # Players guess
    while loop == False: # Runs game
        if guess != ans: #  Lowers tries left
            try_left -= 1
        if try_left == 1: # Ends game after all tries used
            loop = True
        if guess == ans: # Ends game after you win
            print("That took you", 11 - try_left, "tries") # tells you how many tries used
            loop = True
        elif guess >= ans: # tells you your either to high or low
            print("Your guess is to high, you have", try_left, "tries left")
            guess = int(input())
        elif guess <= ans:
            print("Your guess is to low, you have", try_left, "tries left")
            guess = int(input())
    if try_left == 1: # Game over if you lose
        print("GAME OVER")
    print("Would you like to play again, y or n") # instructions
    end = input() # Ending choice
    if end == "y": # If they type y they play again
        hiLo()
    else: # Ends the whole game
        return

def main():
    """This function runs the entire program.
        Once your function is created place it below.
        You may need to provide extra code to run your function several times."""
    hiLo()
# Allows the main function to show up in the terminal once script is executed. 
if __name__ == "__main__":
    main()
