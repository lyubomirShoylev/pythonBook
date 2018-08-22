# Longevity
# Demonstrates text and entry widgets, and the Grid layout manager

from tkinter import *

class Application(Frame):
    """GUI application which can reveal the secrets of longevity."""
    
    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        """Create button, text, and entry widgets."""
        # create instruction label
        self.instLbl = Label(self, text="Enter password for the secret of longevity")
        self.instLbl.grid(row=0, column=0, columnspan=2, sticky=N)

        # create label for password
        self.pwLbl = Label(self, text="Password: ")
        self.pwLbl.grid(row=1, column=0, sticky=W)
        
        # create entry widget to accept password
        self.pwEnt = Entry(self)
        self.pwEnt.grid(row=1, column=1, sticky=W)

        # create submit button
        self.submitBttn = Button(self, text="Submit", command=self.reveal)
        self.submitBttn.grid(row=2, column=0, sticky=W)

        # create text widget to display message
        self.secretTxt = Text(self, width=35, height=5, wrap=WORD)
        self.secretTxt.grid(row=3, column=0, columnspan=2, sticky=W)
    
    def reveal(self):
        """Display message based on password."""
        contents = self.pwEnt.get()
        if contents == "secret":
            message = "Here's the secret to living to 100: live to 99 "\
                      "and then be VERY careful."
        else:
            message = "Thats not the correct password, so I can't share "\
                      "the secret with you."
        self.secretTxt.delete(0.0, END)
        self.secretTxt.insert(0.0, message)

# main
root = Tk()
root.title("Longevity")
root.geometry("300x150")

app = Application(root)

root.mainloop()