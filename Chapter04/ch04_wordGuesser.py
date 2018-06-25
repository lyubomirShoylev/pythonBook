# Word Guesser
#
# The computer chooses a random word, then the player has to
# guesss letters. The computer can only respond with yes or no.
# They have only five tries, after that they should guess
# the word.

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one random word from the sequence
word = random.choice(WORDS)

# start the game
print(
"""
                  Welcome to Word Guesser!

Try to guess the word only knowing its length and some letters!
"""
)
print("\nI have thought of a word. Let's see if you can guess it!")
print(f"First, the word is {len(word)} letters long.")

print("\nNow you will give me a letter and I will tell you if it belongs in the word:")
# Not found the way to make this work yet
# print(
# """
# Letter | In word?
# -------+---------
# """
# )
guess = ""
for i in range(5):
    guess =  input("Your letter: ")
    if guess.lower() in word and not word:
        print(f"Yes, the letter -{guess}- is in the word.")
    else:
        print(f"No, the letter -{guess}- is not in the word.")

guess = (input("\nNow try guess the word: ")).lower()
while guess != word and guess!= "":
    print("Sorry, that's not it.")
    guess = (input("Your guess: ")).lower()

if guess == word:
    print("That's it! You guessed it!\n")
print("Thanks for playing.")


input("\n\nPress the enter key to exit.")