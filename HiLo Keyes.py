import random

guessesTaken = 0

print("hello! what is your name?")
myName = input()

number = random.randint (1,100)
print("well,thats a pretty cool name, anyway I'm thinking of a number between 1and 100.")

while guessesTaken < 10:
    print("take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("your guess is too low")

    if guess > number:
        print ("your guess is too high")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job, you guessed my number in under 10 guesses")


if guess!= number:
    number = str(number)
    print("Sorry you ran out of guesses better luck next time.")


