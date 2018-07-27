# War Game
# 
# A one-card version of the game war, based on modules 'cards' and 'games' as in
# example code from the book.

import games, cards

class WarCard(cards.Card):
    """A War Card."""
    ACE_VALUE = 14

    @property
    def value(self):
        if self.isFaceUp:
            v = self.RANKS.index(self.rank) + 1
            if v == 1:
                v = self.ACE_VALUE
        else:
            v = None
        return v

class WarDeck(cards.Deck):
    """A War Deck."""
    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.cards.append(WarCard(rank, suit))

class WarStack(cards.Hand):
    """A War Player's Hand."""
    def __init__(self,name):
        super(WarStack, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ": " + str(len(self.cards)) + " cards in stack"
        return rep
    
    def addWinner(self, cardsWon):
        for card in cardsWon:
            self.cards.append(card)
    
    def isPlaying:
        return self.cards

class WarPlayer(WarStack):
    """A War Player."""
    def lose(self):
        print(self.name, "loses.")
    
    def win(self):
        print(self.name, "wins.")