# Counter
# 
# Program that counts for the user
# They enter the start, end, and iterator

print("\tCounter Game")

start = int(input("\nEnter the beginning of the sequence: "))
end = int(input("Enter the end of the sequence: "))
iterator = int(input("Enter the amount by which to count: "))

print("\n Your sequence is:")
for i in range(start, end + 1, iterator):
    print(i, end = ' ')

input("\n\nPress the enter key to exit.")