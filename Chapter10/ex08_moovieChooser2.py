# Moovie Chooser 2
# Demonstrates radio buttons

from tkinter import *

class Application(Frame):
    """GUI application for favorite movie type."""
    
    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        """Create widgets for movie type choices"""
        # create description label
        Label(self,
              text = "Choose your favorite type of movie."
              ).grid(row = 0, column = 0, sticky = W)
        
        # create instruction label
        Label(self,
              text = "Select one: "
              ).grid(row = 1, column = 0, sticky = W)
        
        # create variable for single, favorite type of movie
        self.favorite = StringVar()
        self.favorite.set(None)

        # create Comedy radio button
        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    value = "comedy.",
                    command = self.updateText,
                    ).grid(row = 2, column = 0, sticky = W)
        
        # create Drama radio button
        Radiobutton(self,
                    text = "Drama",
                    variable = self.favorite,
                    value = "drama.",
                    command = self.updateText,
                    ).grid(row = 3, column = 0, sticky = W)
        
        # create Romance radio button
        Radiobutton(self,
                    text = "Romance",
                    variable = self.favorite,
                    value = "romance.",
                    command = self.updateText,
                    ).grid(row = 4, column = 0, sticky = W)
        
        # create text field to display result
        self.resultsTxt = Text(self, width = 40, height = 5, wrap = WORD)
        self.resultsTxt.grid(row = 5, column = 0, columnspan = 3)
    
    def updateText(self):
        """Update text area and display user's favorite movie type."""
        message = "Your favorite type of movie is "
        message += self.favorite.get()
        self.resultsTxt.delete(0.0, END)
        self.resultsTxt.insert(0.0, message)

# main
root = Tk()
root.title("Movie Chooser 2")
app = Application(root)
root.mainloop()
