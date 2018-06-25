# Hangman Game
# 
# The classic game of Hangman. The computer picks a random word
# and the player wrong to guess it, one letter at a time. If the player
# can't guess the word in time, the little stick figure gets hanged.

# imports
import random

# constants
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 | /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   |
 |   |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |
----------
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# initialize variables
word = random.choice(WORDS) # the word to be guessed
soFar = "-" * len(word)     # one dash for each letter in word to be guessed
wrong = 0                   # number of wrong guesses player has made
used = []                   # letters already guessed

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and soFar != word:
    print(HANGMAN[wrong])
    print(f"\nYou've used the following letters:\n {used}")
    print(f"\nSo far, the word is:\n {soFar}")

    guess = input("\n\nEnter your guess:")
    guess = guess.upper()

    while guess in used:
        print(f"You've already guessed the letter {guess}")
        guess = input("\n\nEnter your guess:")
        guess = guess.upper()
    
    used.append(guess)

    if guess in word:
        print(f"\nYes! {guess} is in the word")

        # create a new soFar to include guess
        new = ""
        for i in range(0, len(word), 1):
            if guess == word[i]:
                new += word[i]
            else:
                new += soFar[i]
        soFar = new[:]
    else:
        print(f"\nSorry, {guess} isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print(f"The word was {word}")

input("\n\nPress the enter key to exit.")