# Hero's Inventory 2.0
# Demonstrates tuples

# create a tuple with some items and display with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print("\nYour items:")
for item in inventory:
    print(item)

input("\nPress the enter key to exit.")

# get the length of a tuple
print(f"You have {len(inventory)} items in your possesion.")

input("\nPress the enter key to exit.")

# test for membership with in
if "healing potion" in inventory:
    print("You will live another day.")

input("\nPress the enter key to exit.")

# display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print(f"At index {index} is {inventory[index]}")

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("\nEnter the index number to end a slice: "))
print(f"inventory[{start}:{finish}] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to exit.")

# concatenate two tuples
chest = ("gold", "gems")
print("You find a chest. It contains: ")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to exit.")