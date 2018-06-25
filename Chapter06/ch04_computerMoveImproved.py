# 
# I GAVE UP ON THIS PSEUDO-AI SHIT
# 


# Tic-Tac-Toe
# **MODIFIED**
# 
# Plays the game of tic-tac-toe against a human opponent
# 
# MODIFICATION:
# Introduces a MINMAX algorithm for computer decision-making, 
# based on the current state of the board. In case the board is empty,
# the center piece is chosen

# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def displayInstruct():
    """Display game instructions"""
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 0 - 8. The number
    will correspond to the board position as illustrated:

                    0 | 1 | 2
                    --+---+--
                    3 | 4 | 5
                    --+---+--
                    6 | 7 | 8

    Prepare yourself, human. The ultimate battle is about to begin.\n
    """
    )

def askYesNo(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def askNumber(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Determine if player or computer goes first."""
    goFirst = askYesNo("Do you require the first move? (y/n): ")
    if goFirst == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be undoing... I will go first.")
        computer = X
        human = O
    return computer, human

def newBoard():
    """Create new game board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def displayBoard(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "-" * 2 + "+" + "-" * 3 + "+" + "-" * 2)
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "-" * 2 + "+" + "-" * 3 + "+" + "-" * 2)
    print("\t", board[6], "|", board[7], "|", board[8])

def legalMoves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def humanMove(board, human):
    """Get human move."""
    legal = legalMoves(board)
    move = None
    while move not in legal:
        move = askNumber("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("That square is already occupied, foolish human. Choose another.\n")
    print("Fine...")
    return move
    
def nextTurn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

# my version, brokeeeen
def bestMove(board, player1, player2):
    board = board[:]

    for move in legalMoves(board):
        board[move] = player1
        result = winner(board)
        if result == TIE:
            score = 0
        elif result == player1:
            score = 1
        else:
            dummy = bestMove(board, player2, player1)
        board[move] = EMPTY

    return (move, score)

# port of trash.js
def bestestMove(board, player1, player2):
    legMovesAndScores = []
    board = board[:]

    for move in legalMoves(board):
        board[move] = player1
        result = winner(board)
        if result == TIE:
            score = 0
        elif result == player1:
            score = 1
        else:
            kek = bestestMove(board, player2, player1)
            score = -1 * kek[1]
        if score == 1:
            return (move, score)
        board[move] = EMPTY
        legMovesAndScores.append((move, score))
    
    def takeSecond(elem):
        return elem[1]

    legMovesAndScores.sort(key=takeSecond, reverse=True)
    return legMovesAndScores[0]

# ugly
def computerMove(board, computer, human):
    """Make computer move."""
    board = board[:]

    # the best positions to have in case of an empty board
    EMPTY_MOVE = 4

    if len(legalMoves(board)) == 9:
        return EMPTY_MOVE
    else:
        # possibilities, dummy1, dummy2 = bestMove(board, computer, human, [], 0)
        # return possibilities[0][0]
        result = bestestMove(board, computer, human)
        return result[0]

    # scoring of the choice result    

    # print("I shall take square number", end=" ")

    # # if computer can win, take that move
    # for move in legalMoves(board):
    #     board[move] = computer
    #     if winner(board) == computer:
    #         print(move)
    #         return move
    #     # done checking this move, undo it
    #     board[move] = EMPTY
    
    # # if human can win, take that move
    # for move in legalMoves(board):
    #     board[move] = human
    #     if winner(board) == human:
    #         print(move)
    #         return move
    #     # done checking this move, undo it
    #     board[move] = EMPTY
    
    # # since no one can win on next move, pick best open square
    # for move in BEST_MOVES:
    #     if move in legalMoves(board):
    #         print(move)
    #         return move
    return 4

def congratWinner(theWinner, computer, human):
    """Cngratulate the winner."""
    if theWinner != TIE:
        print(theWinner, "won!\n")
    else:
        print("It's a tie!\n")
    
    if theWinner == computer:
        print("As I predicted, human, I am triumphant once more. \n"\
              "Proof that computers are superior to humans in all regards.")
    
    elif theWinner == human:
        print("No, no! It cannot be! Somehow you tricked me, human. \n"\
              "But never again! I, the computer, so swear it!")
    
    elif theWinner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n"\
              "Celebrate today... for this is the best you will ever achieve.")

def main():
    displayInstruct()
    computer, human = pieces()
    turn = X
    board = newBoard()
    displayBoard(board)

    while not winner(board):
        if turn == human:
            move = humanMove(board, human)
            board[move] = human
        else:
            move = computerMove(board, computer, human)
            board[move] = computer
        displayBoard(board)
        turn = nextTurn(turn)
    
    theWinner = winner(board)
    congratWinner(theWinner, computer, human)

# start the program
main()
input("\n\nPress the enter key to quit.")