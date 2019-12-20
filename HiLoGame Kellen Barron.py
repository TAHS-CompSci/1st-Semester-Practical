"""
projectName.py
Programmer: Your Name
Project description
"""
# Your code goes below
import random 

def hiLo_game(): # This defines what is going to happen and what it is going to be doing 
    x = random.randint(1, 100)   # This chooses a random number between 1-100 
    print(x)
    guess = int(input ('guess a number from 1-100: ')) # This prints guess a number 
    
    if guess < x: 
        print("guess too low!") # If the guess is low, it will print guess too low 

    if guess > x: 
        print("guess too high!") # If the guess is high, it will print guess too high 

    if guess == x: 
        
        print ("winner!, want to play again?") # If you guess the number correctly, it will print winner! Then, you can choose to play again or not play again #(That is down here) 
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
