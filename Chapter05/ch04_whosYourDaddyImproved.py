# Who's Your Daddy Improved*
# 
# A program that lets the user enter the name of a male and
# produces the name of his father.The user can add, replace,
# and delete son-father pairs.
# The improvement is that you can now name a person's gradnfather,
# using only the one son-father dictionary

pairs = {
    "BOBBY"   : "ROBERT",
    "DONNY"   : "DANIEL",
    "DICKY"   : "RICHARD",
    "JONNY"   : "JONATHAN",
    "ROBERT"  : "ROBERTO",
    "DANIEL"  : "DANIELO",
    "RICHARD" : "RICCARDO",
    "JONATHAN": "JUAN"
}

choice = None

# print intro
print("\tWelcome to Who's your Daddy!\n")
while choice !="0":
    # print menu
    print("Choices:")
    print(
    """
    0 - Exit
    1 - Name of a father
    2 - Add a son-father pair
    3 - Edit a son-father pair
    4 - Delete a son-father pair
    5 - List all son-father pairs
    6 - Name of a grandfather (on father's line)
    """
    )
    choice = input("\nYour choice: ")

    # exit menu
    if choice == "0":
        print("Thank you for playing!")
        continue

    # son -> parent
    if choice == "1":
        son = input("Whose father are you looking for: ")
        son = son.upper()
        if son == "0":
            print("Exiting...")
            continue
        while son not in pairs:
            print("I don't know who that is, maybe try again?")
            son = input("Whose father are you looking for: ")
            son = son.upper()
        print(f"\nI know that!\nThe father of {son} is {pairs[son]}.\n")

    # add pair
    elif choice == "2":
        son = input("Who do you want to add in the database: ")
        son = son.upper()
        father = input("And who is their father: ")
        father.upper()
        while son in pairs and father == pairs[son]:
            print("The pair is already in the database! Try again\n")
            son = input("Who do you want to add in the database: ")
            son = son.upper()
            father = input("And who is their father: ")
            father.upper()
        pairs[son] = father.upper()
        print("Son-father pair added to the database.\n")

    # edit pair
    elif choice == "3":
        son = input("Who do you want to edit in the database: ")
        son = son.upper()
        while son not in pairs:
            print("I don't know who that is, maybe try again?")
            son = input("Who do you want to edit in the database: ")
            son = son.upper()
        father = input("And who should their father be: ")
        father.upper()
        pairs[son] = father.upper()
    
    # delete pair
    elif choice == "4":
        son = input("Who do you want to delete in the database: ")
        son = son.upper()
        while son not in pairs:
            print("I don't know who that is, maybe try again?")
            son = input("Who do you want to delete in the database: ")
            son = son.upper()
        pairs.pop(son)
        print("Job's done!")
    
    # list pairs
    elif choice == "5":
        print("The pairs are:")
        # print(pairs.items())
        print("   Son  | Father ")
        print("--------+" + "-" * 20)
        for item in pairs:
            print(f" {item:6} | {pairs[item]}")
    
    # name grandfather
    elif choice == "6":
        son = input("Whose grandfather are you looking for: ")
        son = son.upper()
        if son == "0":
            print("Exiting...")
            continue
        while son not in pairs:
            print("I don't know who that is, maybe try again?")
            son = input("Whose grandfather are you looking for: ")
            son = son.upper()
        print(f"\nI know that!\nThe grandfather of {son} is {pairs[pairs[son]]}\n")

    # unknown input
    else:
        print("Not a defined command. Try again!\n\n")

input("\n\nPress the enter key to exit.")