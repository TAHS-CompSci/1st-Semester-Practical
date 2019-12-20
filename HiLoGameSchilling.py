"""
HiLoGameSchilling
Programmer: Cole Schilling
HiLoGame
"""
import random

def HiLo():
    target = random.randint(1,100)
    tries = 10
    guesses = True
    while guesses:
        guess = int(input("Guess any number between 1 thru 100. "))
        if guess == target:
            print('Correct!, do you wish to play again')
            print('tries: ',tries,)
        if guess < target:
            tries-=1
            print("Higher!")
            print('tries: ',tries,)
            if tries == 0:
                print('game over.. better luck next time')
                guesses = False
        if guess > target:
            tries-=1
            print("Lower")
            print('tries: ',tries,)
            if tries ==0:
                print('game over.. better luck next time')
                guesses = False