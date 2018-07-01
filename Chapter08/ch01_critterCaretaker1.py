# Critter Caretaker - 1
# 
# A virtual pet to take care of
# **The amount of food/play affects how quickly the levels drop

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.hungerTick = 1
        self.boredomTick = 1
    
    def __passTime(self):
        # the passage of time is self-regulated based on the amount of play/food
        self.hunger += self.hungerTick
        self.boredom += self.boredomTick
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <=10:
            m = "okay"
        elif 11<= unhappiness <=15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print(f"I'm {self.name} and I feel {self.mood} now.\n")
        self.__passTime()
    
    def eat(self, food = 4):
        print("Brruppp. Thank you.")
        self.hunger -= food
        self.hungerTick = max(food // 4, 1)
        if self.hunger < 0:
            self.hunger = 0
        self.__passTime()
    
    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        self.boredomTick = max(fun // 4, 1)
        if self.boredom < 0:
            self.boredom = 0
        self.__passTime()

def main():
    critName = input("What do you want to name your critter?: ").upper()
    crit = Critter(critName)

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()
        
        # exit
        if choice == "0":
            print("Good-bye.")
        
        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            amount = int(input("\n\tHow much food you want to feed? "))
            crit.eat(amount)
        
        # play with your critter
        elif choice == "3":
            amount = int(input("\n\tFor how much do you want to play? "))
            crit.play(amount)
        
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the enter key to exit")