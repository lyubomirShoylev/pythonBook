# Coin Flipper
#
# Flips a coin 100 times, then tells you the number of
# heads and tails.

import random

coin = 0 #initialize the coin value
count = 0 # counter of flips

# counters of heads and tails
heads = 0
tails = 0

# to be considered - is it a fair thing?
while count < 100:
    coin = random.randint(1,100)
    if coin <= 50:
        heads += 1
    elif coin > 50:
        tails += 1
    count += 1

print(f"The coin flipped {heads} heads and {tails} tails.")

input("\n\nPress the enter key to exit.")


