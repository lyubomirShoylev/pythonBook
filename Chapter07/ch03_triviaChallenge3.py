# Trivia Challenge - 3
# 
# Trivia game that reads a plain text file
# A highscore system, saving it in a plain text file

import sys, pickle

def openFile(filename, mode):
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
    try:
        points = int(nextLine(theFile))
    except:
        points = None
    # if points:
    #     points = points[0]
    
    explanation = nextLine(theFile)

    return category, question, answers, correct, points, explanation

def highScores(name, score):
    """Puts the player's score in the highscore board if possible."""
    # read the highscores table from file
    flag = False
    scoresFile = openFile("highscores.txt", "r")
    scoresList = []
    varName = scoresFile.readline()
    varScore = int(scoresFile.readline())
    while varName != "":
        scoresList.append((varName, varScore))
        varName = scoresFile.readline()
        try:
            varScore = int(scoresFile.readline())
        except:
            varScore = None
    # scoresFile.close()

    # insert the score in the table if possible
    for i in range(len(scoresList)):
        if score > scoresList[i][1]:
            scoresList.insert(i, (name + "\n", score))
            flag = True
    
    # shows the user the updated table
    scoresList = scoresList[:10]
    print(scoresList)

    # save changes
    scoresFile = openFile("highscores.txt", "w")
    # pickle.dump(scoresList, scoresFile)
    for i in scoresList:
        scoresFile.write(i[0])
        scoresFile.write(str(i[1]) + "\n")
    scoresFile.close()

def welcome(title):
    """Welcome the player and their name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print(f"\t\t{title}\n")

def main():
    triviaFile = openFile("trivia3.txt", "r")
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

    name = input("\nNow, may I have your name? ").upper()
    highScores(name, score)

main()
input("\n\nPress the enter key to exit.")