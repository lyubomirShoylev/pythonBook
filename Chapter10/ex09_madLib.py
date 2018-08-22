# Mad Lib
# Create a story based on user input

from tkinter import *

class Application(Frame):
    """GUI application that creates a story based on user input."""
    
    def __init__(self, master):
        """Initialize Frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        """Create widgets to get story information and to display story."""
        # create instruction label
        Label(self,
              text = "Enter information for a new story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        # create a label and text entry for the name of a person
        Label(self,
              text = "Person: "
              ).grid(row = 1, column = 0, sticky = W)
        self.personEnt = Entry(self)
        self.personEnt.grid(row = 1, column = 1, sticky = W)

        # create a label and text entry for a plural noun
        Label(self,
              text = "Plural noun: "
              ).grid(row = 2, column = 0, sticky = W)
        self.nounEnt = Entry(self)
        self.nounEnt.grid(row = 2, column = 1, sticky = W)
        
        # create a label and text entry for a verb
        Label(self,
              text = "Verb: "
              ).grid(row = 3, column = 0, sticky = W)
        self.verbEnt = Entry(self)
        self.verbEnt.grid(row = 3, column = 1, sticky = W)

        # create a label for adjectives check button
        Label(self,
              text = "Adjective(s): "
              ).grid(row = 4, column = 0, sticky = W)
        
        # create itchy check button
        self.isItchy = BooleanVar()
        Checkbutton(self,
                    text = "itchy",
                    variable = self.isItchy
                    ).grid(row = 4, column = 1, sticky = W)
        
        # create joyous check button
        self.isJoyous = BooleanVar()
        Checkbutton(self,
                    text = "joyous",
                    variable = self.isJoyous
                    ).grid(row = 4, column = 2, sticky = W)
        
        # create electric check button
        self.isElectric = BooleanVar()
        Checkbutton(self,
                    text = "electric",
                    variable = self.isElectric
                    ).grid(row = 4, column = 3, sticky = W)
        
        # create a label for body parts radio buttons
        Label(self,
              text = "Body Part:"
              ).grid(row = 5, column = 0, sticky = W)
        
        # create variable for single body part
        self.bodyPart = StringVar()
        self.bodyPart.set(None)
        
        # create body part radio buttons
        bodyParts = ["bellybutton", "big toe", "medulla oblongata"]
        column = 1
        for part in bodyParts:
            Radiobutton(self,
                        text = part,
                        variable = self.bodyPart,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1
        
        # create a submit button
        Button(self,
               text = "Click for story",
               command = self.tellStory
               ).grid(row = 6, column = 0, sticky = W)
        
        self.storyTxt = Text(self, width = 75, height = 10, wrap = WORD)
        self.storyTxt.grid(row = 7, column = 0, columnspan = 4)
    
    def tellStory(self):
        """Fill text box with new story based on user input."""
        # get values from the GUI
        person = self.personEnt.get()
        noun = self.nounEnt.get()
        verb = self.verbEnt.get()
        adjectives = ""
        if self.isItchy.get():
            adjectives += "itchy, "
        if self.isJoyous.get():
            adjectives += "joyous, "
        if self.isElectric.get():
            adjectives += "electric, "
        bodyPart = self.bodyPart.get()

        # create the story
        story = "The famous explorer "
        story += person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += "when one day, the "
        story += noun
        story += " found "
        story += person + ". "
        story += "A strong, "
        story += adjectives
        story += "peculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += bodyPart + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured"
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."
        
        # display the story
        self.storyTxt.delete(0.0, END)
        self.storyTxt.insert(0.0, story)

# main
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()
