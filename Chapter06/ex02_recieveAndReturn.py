# Recieve and Return
# Demonstrates parameters and return values

def display(message):
    print(message)

def giveMeFive():
    five = 5
    return five

def askYesNo(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("Y", "N"):
        response = input(question).lower()
    return response

# main
display("Here's a message for you.\n")

number = giveMeFive()
print("Here's what I got from giveMeFive():", number)

answer = askYesNo("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)

input("\n\nPress the enter key to exit.")