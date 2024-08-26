# Number guessing game
import random

def random_number():
    hidden_number = random.randint(1, 10)

    input = 0
    while input != hidden_number:
        input = int(input("Enter a number between 1 and 10: "))
        if input < hidden_number:
            print("Your guess is too low")
        elif input > hidden_number:
            print("Your guess is too high")

    print("Correct!")

random_number()