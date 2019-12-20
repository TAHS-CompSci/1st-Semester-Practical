"""
projectName.py
Programmer: Your Name
Project description
"""
# Your code goes below



def main():
    """This function runs the entire program.
        Once your function is created place it below.
        You may need to provide extra code to run your function several times."""
import random
number = random.randint(1,100)
def HiLo():
    tries=10
    guesses= True 
    while guesses:
        guess=int(input('Guess my number: '))
        if guess == number:
            guesses = False
            multiple = input('thats my number alright! Want to play again?: ')
            if multiple== 'yes':
                HiLo()
            if multiple== 'no':
                print ('Sorry please come again')
                break
        if guess < number:
            tries-=1    
            if tries == 0:
                print('Game Over')
                option=input('Want to play again?: ')
                if option == ('yes'):
                    print ('great!')
                    HiLo()
                if option == ('no'):
                    print ('Im so sorry come again!')
                    break
                guesses = False 
            print ('too low! try again')
            print ('tries:', tries)
        if guess > number:
            tries-=1
            if tries == 0:
                print('Game Over')
                option=input('Want to play again?: ')
                if option == ('yes'):
                    print ('great!')
                    Hilo()
                if option == ('no'):
                    print ('Im so sorry come again!')
                    break
                guesses = False 
            print ('thats pretty high!')
            print ('tries:', tries)

# Allows the main function to show up in the terminal once script is executed. 
if __name__ == "__main__":
    main()
