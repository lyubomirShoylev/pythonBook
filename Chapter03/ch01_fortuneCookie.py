# Fortune Cookie Simulator
#
# Displays one random fortune out of five possibilities

import random

cookie = random.randint(1,5)

if cookie == 1:
    print("Fortune1")
elif cookie == 2:
    print("Fortune2")
elif cookie == 3:
    print("Fortune3")
elif cookie == 4:
    print("Fortune4")
elif cookie == 5:
    print("Fortune5")
else:
    print("You are far wiser than me, I cannot pass you any fortune.")

input("\n\nPress the enter key to exit.")


