# Message Analyzer
# Demonstrates the len() function and the in operator

message = input("Enter a word: ")

print(f"The length of your message is: {len(message)}")

print("\nThe most common letter in the English language, 'e',", end = ' ')
if 'e' in message:
    print("is in your message.")
else:
    print("is not in your message.")

input("\n\nPress the enter key to exit.")