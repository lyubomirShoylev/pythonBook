# List Random
# The program prints a list of words in random order
# while not repeating any.

import random

WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# to be used
words = list(WORDS[:])

while words:
    out = random.choice(words)
    print(out, end = " ")
    words.remove(out)

print("\n\nThat's all folks!")

input("\nPress the enter key to exit.")