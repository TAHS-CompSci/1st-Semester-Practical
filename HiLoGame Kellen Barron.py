"""
projectName.py
Programmer: Your Name
Project description
"""
# Your code goes below
import random 

def hiLo_game(): # This defines what it will be doing 
    x = random.randint(1, 100)  # This chooses a random number  
    tries = 1
    print(x)
    booli = True
    guess = int(input ('guess a number from 1-100: '))
    while booli == True:
        if guess < x: 
            print("guess too low!")   # These are the loops 
            tries += 1
            guess = int(input ('guess a number from 1-100: '))
        if guess > x: 
            print("guess too high!")   # Guess too low, it will print too low. Guess is too high, it will print guess too high. Ig guess is correct, it will print winner and we can choose if we want to play again. 
            tries =+ 1
            guess = int(input ('guess a number from 1-100: '))
        if guess == x: 
            print ("winner!, want to play again?") 
            tries += 1
            booli = False
        if tries == 10:
            print("You Lose")
            booli = False
    print("Would you like to play again")
    answer = input ("Yes or No: ")    
    if answer == "Yes":
        hiLo_game()
    if answer == "No":
        return
    
hiLo_game() 
      


def main():
    """This function runs the entire program.
        Once your function is created place it below.
        You may need to provide extra code to run your function several times."""
    hiLo_game()

# Allows the main function to show up in the terminal once script is executed. 
if __name__ == "__main__":
    main()
