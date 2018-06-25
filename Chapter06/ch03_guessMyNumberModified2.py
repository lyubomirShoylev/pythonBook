# Guess My Number
# **MODIFIED**
# **MODIFIED 2**
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money. In this version of the game
# the player has limited amount of turns.
# 
# MODIFICATION:
# Reusing the function askNumber from Chapter06 in order to exercise
# function usage and reusability
# MODIFICATION 2:
# Putting the rest of the function in a main() function

import random

# ask the user for a number in a certain range
def askNumber(question, theNumber, low, high, step = 1):
    """
    askNumber(question, low, high[, step])\n
    Ask for a number within a range. Optional step is available, and the default
    value is 1.
    """
    counter = 0
    response = None
    while response not in range(low, high, step):
        counter += 1
        response = int(input(question))
        if response > theNumber:
            print("Lower...")
        elif response < theNumber:
            print("Higher...")
    return response, counter

def main():
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in under fifteen attempts if possible.\n")

    # set the inital values
    theNumber = random.randint(1,100)
    # guess = int(input("Take a guess: "))
    guess = None
    tries = 0

    # guessing loop
    while guess != theNumber and tries < 15:
        # if guess > theNumber:
        #     print("Lower...")
        # else:
        #     print("Higher...")
        guess, counter = askNumber("Take a guess: ", theNumber, 1, 101)
        
        # guess = int(input("Take a guess: "))
        tries += counter

    if guess == theNumber:
        print(f"\nYou guessed it! The number was {theNumber}")
        print(f"And it only took you {tries} tries!\n")
    else:
        print(f"\nYou failed! You know there is an actual strategy?")
        print("Anyway, better luck next time!")


# start the program
main()

input("\n\nPress the enter key to exit.")