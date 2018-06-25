# Character Creator
# 
# A character creator for a role-playing game. The player is given
# a pool of 30 points to spend on four attributes: Strength, Healt,
# Wisdom, and Dexterity. The player is able to spend points from the pool
# take points back from an attribute back to the pool.

# initialize variables
pool = 30
attributes = [("Strength", 0), ("Health", 0), 
              ("Wisdom", 0), ("Dexterety", 0)]

# start the program
print("\tWelcome to the Character Creator!")

print("\nYour character's point are:")
print(" # | Attribute | Points")
print("---+-----------+-------")
for i in range(len(attributes)):
    print(f"{i:>2} | {attributes[i][0]:>9} | {attributes[i][1]:>3}")

while True:
    print(f"\nYou have {pool} points left.")
    print("\nYou have three options:")
    print("\t0 - Exit\n\t1 - Spend points\n\t2 - Remove points")
    choice = input("\nWhat do you want to do?:")

    # exiting the program
    if choice == "0":
        if pool != 0:
            print("\nYou haven't spent all your points!")
            input("Press enter to return to the menu.")
            continue
        elif pool == 0:
            print("\nThank you for using us!")
            break
    
    # assining points to an attribute
    elif choice == "1":
        print("\nYour character's point are:")
        print(" # | Attribute | Points")
        print("---+-----------+-------")
        for i in range(len(attributes)):
            print(f"{i:>2} | {attributes[i][0]:>9} | {attributes[i][1]:>3}")
        
        att = int(input("\nWhich attribute to assign? "))
        pts = int(input("How many points to assign? "))
        while (pool - pts) < 0:
            print("Not a valid value - you don't have that many points.")
            pts = input("How many points to assign? ")
        
        pool -= pts
        attributes[att - 1] = ((attributes[att - 1][0]),(attributes[att - 1][1] + pts))
        input("\nPress enter to return to the menu.")

    # removing points from an attribute
    elif choice == "2":
        print("\nYour character's point are:")
        print(" # | Attribute | Points")
        print("---+-----------+-------")
        for i in range(len(attributes)):
            print(f"{i:>2} | {attributes[i][0]:>9} | {attributes[i][1]:>3}")
            
        att = int(input("\nFrom which attribute to remove? "))
        pts = int(input("How many points to remove? "))
        change = attributes[att - 1]
        while (change[1] - pts) < 0:
            print("Not a valid value - you have't that many points in this attribute.")
            pts = input("How many points to remove? ")
        
        pool += pts
        change = (change[0], change[1] - pts)
        attributes[att - 1] = change
        input("\nPress enter to return to the menu.")

input("\n\nPress the enter key to exit.")