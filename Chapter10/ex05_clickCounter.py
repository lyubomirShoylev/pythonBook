# Click Counter
# Demonstrates binding an event with an event handler

from tkinter import *

class Application(Frame):
    """GUI application which counts button clicks."""
    
    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0    # the number of button clicks
        self.createWidget()
    
    def createWidget(self):
        """Create button which displays number of clicks."""
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.updateCount
        self.bttn.grid()
    
    def updateCount(self):
        """Increase click count and display new total"""
        self.bttn_clicks += 1
        self.bttn["text"] = f"Total Clicks: {self.bttn_clicks}"

# main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()
