# Trivia Challenge - 1
# 
# Trivia game that reads a plain text file

import sys

def open_file(filename, mode):
    """Open a file."""
    try:
        theFile = open(filename, mode)
    except IOError as e:
        print(f"Unable to open the file {filename}. Ending program.\n{e}")
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return theFile

def nextLine(theFile):
    """Return next line from the trivia file, formatted."""
    line = theFile.readline()
    line = line.replace("/", "\n")
    return line

def nextBlock(theFile):
    """Return the next block of data from the trivia file."""
    category = nextLine(theFile)

    question = nextLine(theFile)

    answers = []
    for i in range(4):
        answers.append(nextLine(theFile))
    
    correct = nextLine(theFile)
    if correct:
        correct = correct[0]
    
    points = nextLine(theFile)
    if points:
        points = points[0]
    
    explanation = nextLine(theFile)

    return category, question, answers, correct, points, explanation

def welcome(title):
    """Welcome the player and their name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print(f"\t\t{title}\n")

def main():
    triviaFile = open_file("trivia1.txt", "r")
    title = nextLine(triviaFile)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, points, explanation = nextBlock(triviaFile)
    while category:
        # ask a category
        print(category)
        print(question)
        for i in range(4):
            print(f"\t {i + 1} - {answers[i]}")
        
        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += points
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score: {0}\n\n".format(score))

        # get next block
        category, question, answers, correct, points, explanation = nextBlock(triviaFile)
    
    triviaFile.close()

    print("That was the last question!")
    print(f"Your final score is {score}")

main()
input("\n\nPress the enter key to exit.")