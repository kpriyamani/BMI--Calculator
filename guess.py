#number_guess.py
import random
number=random.randint(1,50)
guess=None
while guess!=number:
    guess=int(input("Guess a number between 1 and 50:"))
    if guess<number:
        print("Too low!")
    elif guess>number:
        print("Too high!")
    else:
        print("Congratulations! you guessed it!")
