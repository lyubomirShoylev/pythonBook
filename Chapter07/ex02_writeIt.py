# Write It
# Demonstrates writing to a text file

print("Creating a text file with the write() method")
textFile = open("writeIt.txt", "w")
textFile.write("Line 1\n")
textFile.write("This is line 2\n")
textFile.write("That makes this line 3\n")
textFile.close()

print("\nReading the newly created file.")
textFile = open("writeIt.txt", "r")
print(textFile.read())
textFile.close()

print("\nCreating a text file with the writelines() method.")
textFile = open("writeIt.txt", "w")
lines = ["Line 1\n",
         "This is line 2\n",
         "That makes this line 3\n"]
textFile.writelines(lines)
textFile.close()

print("\nReading the newly created file.")
textFile = open("writeIt.txt", "r")
print(textFile.read())
textFile.close()

input("\n\nPress the enter key to exit.")