# Private Critter
# Demonstrates private variables and methods

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name        # public attribute
        self.__mood = mood      # private attribute
    
    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")
    
    def __privateMethod(self):
        print("This is a private method.")
    
    def publicMethod(self):
        print("This is a public method.")
        self.__privateMethod()

# main
crit = Critter(name = "Poochie", mood = "happy")
crit.talk()
crit.publicMethod()

input("\n\nPress the enter key to exit.")