# Playing Cards
# Demonstrates combining objects

class Card(object):
    """A playing card."""
    RANKS = ["A", "1", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        rep = self.rank+self.suit
        return rep

class Hand(object):
    """A hand of playing cards."""
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep
    
    def clear(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)
    
    def give(self, card, otherHand):
        self.cards.remove(card)
        otherHand.add(card)

# main
card1 = Card(rank = "A", suit = "c")
print("Printing a card object:")
print(card1)

card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c")
print("\nPrinting the rest of the objects individually:")
print(card2)
print(card3)
print(card4)
print(card5)

myHand = Hand()
print("\nPrinting my hand before I add any cards:")
print(myHand)

myHand.add(card1)
myHand.add(card2)
myHand.add(card3)
myHand.add(card4)
myHand.add(card5)
print("\nPrinting my hand after adding 5 cards:")
print(myHand)

yourHand = Hand()
myHand.give(card1, yourHand)
myHand.give(card2, yourHand)
print("\nGave the first two cards from my hand to your hand.")
print("Your hand:")
print(yourHand)
print("My hand:")
print(myHand)

myHand.clear()
print("\nMy hand after cleaning it:")
print(myHand)

input("\n\nPress the enter key to exit.")