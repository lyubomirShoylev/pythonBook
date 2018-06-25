# Car Salesman
#
# The following program calculates the price of
# commission of a car salesman based on the base car
# price, entered by the user. The commission includes
# the following fees: tax and license (percentage based),
# and dealer prep and destination charge(fixed).

basePrice = float(input("What is the base price of the car? "))

tax = basePrice * 0.15
license = basePrice * 0.05
dealerPrep = 500
destinationCharge = 500

actualPrice = basePrice + tax + license + dealerPrep + destinationCharge
print("The actual price after applying fees is:", actualPrice)

input("\nPress the enter key to exit.")









