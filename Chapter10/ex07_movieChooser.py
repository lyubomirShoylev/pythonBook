# Moovie Chooser
# Demonstrates check buttons

from tkinter import *

class Application(Frame):
    """GUI application for favorite movie types."""
    
    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        """Create widgets for movie type choices."""
        # create description label
        Label(self,
              text = "Choose your favorite movie types."
              ).grid(row = 0, column = 0, sticky = W)
        
        # create instruction label
        Label(self,
              text = "Select all that apply: "
              ).grid(row = 1, column = 0, sticky = W)\
        
        # create Comedy check button
        self.likesComedy = BooleanVar()
        Checkbutton(self,
                    text = "Comedy",
                    variable = self.likesComedy,
                    command = self.updateText
                    ).grid(row = 2, column = 0, sticky = W)
        
        # create Drama check button
        self.likesDrama = BooleanVar()
        Checkbutton(self,
                    text = "Drama",
                    variable = self.likesDrama,
                    command = self.updateText
                    ).grid(row = 3, column = 0, sticky = W)
        
        # create Romance check button
        self.likesRomance = BooleanVar()
        Checkbutton(self,
                    text = "Romance",
                    variable = self.likesRomance,
                    command = self.updateText
                    ).grid(row = 4, column = 0, sticky = W)
        
        # create text field to display reuslts
        self.resultsTxt = Text(self, width = 40, height = 5, wrap = WORD)
        self.resultsTxt.grid(row = 5, column = 0, columnspan = 3)
    
    def updateText(self):
        """Update text widget and display user's favorite movie types."""
        likes = ""

        if self.likesComedy.get():
            likes += "You like comedic movies.\n"
        
        if self.likesDrama.get():
            likes += "You like dramatic movies.\n"
        
        if self.likesRomance.get():
            likes += "You like romantic movies.\n"
        
        self.resultsTxt.delete(0.0, END)
        self.resultsTxt.insert(0.0, likes)

# main
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()
