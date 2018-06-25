# Print Backwards Program
#
# The user enters a string, the program prints it
# backwards. Simple stuff

word = input("Enter a word: ")

output = ""
for i in range(len(word)):
    output = word[0] + output
    word = word[1:]

print(f"\nYour word backward is: {output}")

input("\n\nPress the enter key to exit.")