# No Vowels
# Demonstrates creating new strings with a for loop

message = input("Enter a message: ")
newMessage = ""
VOWELS = "aeiou"

print()
for letter in message:
    # letter.lower() assures it could be from VOWELS
    if letter.lower() not in VOWELS:
        newMessage += letter
        print("A new string has been created:", newMessage)

print("\n Your message without vowels is:", newMessage)

input("\n\nPress the enter key to exit.")