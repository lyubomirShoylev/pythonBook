# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money. In this version of the game
# the player has limited amount of turns.

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in under fifteen attempts if possible.\n")

# set the inital values
theNumber = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != theNumber and tries < 15:
    if guess > theNumber:
        print("Lower...")
    else:
        print("Higher...")
    
    guess = int(input("Take a guess: "))
    tries += 1

if guess == theNumber:
    print(f"\nYou guessed it! The number was {theNumber}")
    print(f"And it only took you {tries} tries!\n")
else:
    print(f"\nYou failed! You know there is an actual strategy?")
    print("Anyway, better luck next time!")

input("\n\nPress the enter key to exit.")