# Guess My Number Reversed
# 
# The player enters a number betweem 1 and 100
# The computer trys to guess it by using an efficient
# algorithm known as binary search, while the user guides
# it, telling if it has a "guess" that is too high, too 
# low, or right on the money

# note: the author has probably intended us to use the
# RNG libraries as previously in the chapter, however,
# we will disobey :D

print("\tWelcome to 'Guess My Number'! Now Reversed TM")
print("\nYou think of a number between 1 and 100.")
print("I will try to guess it in as few attempts as possible.\n")

playerNum = int(input("Enter your number: "))

# setting up the variables for the binary
uppRange = 100
lowRange = 1
middle = 0
# tries counter
tries = 0

while True:
    middle = (uppRange + lowRange)//2
    ans = input(f"Is {middle} your number?[Y|h|l]")
    if (not ans) or ans.lower() == 'y':
        tries += 1
        break
    elif ans.lower() == 'h':
        uppRange = middle
        tries += 1
    elif ans.lower() == 'l':
        lowRange = middle
        tries += 1
    else:
        print("Invalid input!")

if middle == playerNum:
    print(f"See, not that hard! It took me only {tries} tries!")
else:
    print("Why do you have to lie to me bro!")

input("\n\nPress the enter key to exit.")