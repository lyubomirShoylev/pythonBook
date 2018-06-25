# Word Jumble Improved
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
# This version also includes hints in case the player is stuck
# There is also a scoring system

import random

# create a sequence of words and hints to choose from
WORDS = (("python", "A popular programming language"),
         ("jumble", "It's in the name of the game"),
         ("easy", "A level of difficulty of a task"),
         ("difficult", "Tough and not easy"),
         ("answer", "The thing given after a question"),
         ("xylophone", "A musical instrument"))

# pick one random word+hint from the sequence
choice = random.choice(WORDS)
word = choice[0]
hint = choice[1]

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# initialize some variables
counter = 0
usedHint = False
score = 0

# start the game
print(
"""
          Welcome to Word Jumble!

   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print(f"The jumble is: {jumble}")

guess = (input("\nYour guess: ")).lower()
counter += 1
while guess != correct and guess!= "":
    print("Sorry, that's not it.")

    # promp the user offering help
    if counter >= 3:
        ans = input(f"Do you need a hint?[y|N]")
        if ans.lower() == 'y':
            print(hint)
            counter = 0
            usedHint = True
    
    guess = (input("Your guess: ")).lower()
    counter += 1

# calculate score
if usedHint:
    score = max(0, 500 - 50 * (counter - 1))
else:
    score = max(0, 500 - 100 * (counter - 1))

if guess == correct:
    print(f"That's it! You guessed it!\nIt took you only {counter} tries!")
    print(f"Your score is {score}.")
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")