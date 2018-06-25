# Favorite foods
#
# Allows the user to enter their favorite two foods
# and diplays a new food by joining the original 
# names together

print("Which are your two favorite foods?")
foodOne = input("\nFood number one: ")
foodTwo = input("Food number two: ")

print("There is a chance that you might like \"" 
    + foodOne + foodTwo.capitalize() + "\"?" )

input("\nPress the enter key to exit.")