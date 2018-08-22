# Guess My Number GUI
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money. This version of the game uses
# a GUI instead of a terminal-based interface.
# (The game follows the functionality of Chaptere03/ex10_guessMyNumber.py)

import random
from tkinter import *

class Application(Frame):
    """GUI application based on Guess My Number game."""

    def __init__(self, master):
        """Initialize frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.tries = 0
        self.theNumber = random.randint(1,100)
        self.createWidgets()
    
    def createWidgets(self):
        """Create widgets to see the player input"""
        # instrucrion label
        Label(self,
              text = "I'm thinking of a number between 1 and 100.\n" +
              "Try to guess it in as few attempts as possible."
              ).grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = W)
        
        # create label for the guessing of the number
        Label(self,
              text = "Take a guess: "
              ).grid(row = 2, column = 0, sticky = W)
        
        # create an entry for the guessing
        self.numberEntry = Entry(self)
        self.numberEntry.grid(row = 2, column = 1, sticky = W)
        
        # create a guess button
        Button(self,
               text = "Guess the number",
               command = self.takeGuess
               ).grid(row = 3, column = 0, sticky = W)
        
        self.progOut = Text(self, width = 40, height = 5, wrap = WORD)
        self.progOut.grid(row = 4, column = 0, columnspan = 2, sticky = W)
    
    def takeGuess(self):
        """Checks to see if the user guessed the number correctly."""
        # get the user input
        number = int(self.numberEntry.get())

        # update the number of guesses the person took
        self.tries += 1
        
        if number == self.theNumber:
            message = f"You guessed it! The number was {self.theNumber}!\n" +\
                      f"And it only took you {self.tries} tries!"
        elif number > self.theNumber:
            message = f"Lower...\nNumer of tries: {self.tries}"
        elif number < self.theNumber:
            message = f"Higher...\nNumer of tries: {self.tries}"
        
        self.progOut.delete(0.0, END)
        self.progOut.insert(0.0, message)

# main
root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()
