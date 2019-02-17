import time
import random

# Variables
welcomemsg = "Welcome To The Game."
msg = welcomemsg.split()

# Welcome message
for word in msg:
    print(word)
    time.sleep(.5)

# Ask player for a name
first_name = input("Please Enter Your Name: ")

# Check if user entered SOMETHING and if so, welcome them and initialize the game
if not first_name:
    print("Don't come back")
else:
    print("Hi there {}.".format(first_name))
    ready = input("Are you ready?: Y/N  ")
    if ready.lower() == "y":
        print("I'm thinking of a number between 1-10. You've got 3 chances to guess it")
    else:
        print("I need a name")

# Pause
time.sleep(2)


# Game function
while first_name:
    if guesses <= 0:
        print("GAME OVER! Better luck next time {}".format(first_name))
        time.sleep(1)
        exit()

    else:
        right_number = random.randint(1, 11)
        guess = int(input("What is your guess, {}?  ".format(first_name)))
        if guess >= 11:
            raise ValueError("Input number is too high")
        elif guess <= 0:
            raise ValueError("Input number is too low")
        if guess > right_number:
            print("You guessed to high, try again")
        elif guess < right_number:
            print("You guessed to low, try again")

        if guess == right_number:
            print("Hey, you must be lucky!")
            time.sleep(0.5)
            print("The Game will now terminate. Thanks for playing!")
            time.sleep(1)
            exit()
        else:
            guesses = guesses - 1
            if guesses == 1:
                gissningar = "guess"
            if guesses != 0:
                print("You only have {} {} now, though.".format(guesses, gissningar))