from ast import If
from random import randrange
number = randrange(10)
chances = 0
while chances < 5:
    guess = int(input("enter a number between 1 - 9 "))
    if guess == number:
        print("Congratulations! You won")
        break
    elif guess<number:
        print("your guess was too low")
    elif guess>number:
        print("your guess was too high")
    chances = chances + 1

if chances == 5:
    print("You lost")
