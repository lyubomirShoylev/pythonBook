# Read It
# Demonstrates reading from a text file

print("Opening and closing the file.")
textFile = open("readIt.txt", "r")
textFile.close()

print("\nReading characters from the file.")
textFile = open("readIt.txt", "r")
print(textFile.read(1))
print(textFile.read(5))
textFile.close()

print("\nReading the entire file at once.")
textFile = open("readIt.txt", "r")
wholeThing = textFile.read()
print(wholeThing)
textFile.close()

print("\nReading characters from a line.")
textFile = open("readIt.txt", "r")
print(textFile.readline(1))
print(textFile.readline(5))
textFile.close()

print("\nReading one line at a time")
textFile = open("readIt.txt", "r")
print(textFile.readline())
print(textFile.readline())
print(textFile.readline())
textFile.close()

print("\nReading the entire file into a list.")
textFile = open("readIt.txt", "r")
lines = textFile.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
textFile.close()

print("\nLooping through the file, line by line.")
textFile = open("readIt.txt", "r")
for line in textFile:
    print(line)
textFile.close()

input("\n\nPress the enter key to exit.")