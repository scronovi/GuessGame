import time
import random

# Variables
welcomemsg = "Welcome To The Game."
msg = welcomemsg.split()
score = 0
guesses = 0
right_number = random.randint(1, 11)


# Welcome message
for word in msg:
    print(word)
    time.sleep(.5)

# Ask player for a name
first_name = input("Please Enter Your Name: ")

# Check if user entered SOMETHING and if so, welcome them and initialize the game
if not first_name:
    print("No username entered.")
    exit()
else:
    print("Hi there {}.".format(first_name))
    ready = input("Are you ready?: Y/N  ")
    if ready.lower() == "y":
        print("Okay. I'm thinking of a number between 1-10. "
              "\nLet's see how many tries it takes for you to guess it.")
    else:
        print("Okay. Come back when you are.")
        exit()

# Pause
time.sleep(2)

# Game function
while first_name:
    try:
        guess = int(input("What is your guess, {}?  ".format(first_name)))
        if guess >= 11:
            raise ValueError
        elif guess <= 0:
            raise ValueError
    except ValueError:
        print("You need to enter a number between 1-10! Don't worry, I won't count this.")
    else:
        if guess > right_number:
            print("You guessed to high, try again")
        elif guess < right_number:
            print("You guessed to low, try again")
        if guess == right_number:
            score = guesses
            print("Good job! You guessed a total of {} times.".format(score + 1))
            time.sleep(0.5)
            print("The Game will now terminate. Thanks for playing!")
            time.sleep(1)
            exit()
        else:
            guesses = guesses + 1
            print("Total number of tries: {}".format(guesses))