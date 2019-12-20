"""
projectName.py
Programmer: Your Name
Project description
"""
# Your code goes below
import random

def hiLo(): #This allows the program to allow you to guesss
    x = random.randint(1, 100)
    tries = 9  # There are ten guesses allowed so its like a signma notation since we start at 0
    guess = 0
    loop = True # I ran into problems with the program repeating and not allowing the repeating to stop, so I put a loop and expiremented for a long while before I could get this to work. 
    print ("I am thinking of a number between 1 and 100.")
    print ("You have 10 tries before you lose.")
    guess = int(input("Guess a number between 1 and 100: "))
    while loop:
        if guess > x:
            print ("Guess was higher than actual answer")
            guess = int(input("Guess a number between 1 and 100: "))
            tries -= 1
        elif guess < x:
            print ("Guess was lower than actual answer")
            guess = int(input("Guess a number between 1 and 100: "))
            tries -= 1
        if tries == 0:
            print (" Im sorry, you have lost, would you like to play again?")
            print (" The number was...", x)
            loop = False
        if guess == x:
            print("YOU WIN, Would you like to play again")
            tries -= 1
            loop = False
    answer = input('Yes or No: ')
    if answer == "Yes":
        hiLo()
    if answer == "No":
        return
        
hiLo()


def main():
    """This function runs the entire program.
        Once your function is created place it below.
        You may need to provide extra code to run your function several times."""
    hiLo()

# Allows the main function to show up in the terminal once script is executed. 
if __name__ == "__main__":
    main()
