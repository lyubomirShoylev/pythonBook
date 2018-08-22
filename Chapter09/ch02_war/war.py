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
            v = self.RANKS.index(self.rank)
            if v == 0:
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
    def __init__(self, name):
        super(WarStack, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ": " + str(len(self.cards)) + " cards in stack"
        return rep
    
    # same as pop, but removes the first card
    def pipCard(self):
        c = self.cards[0]
        self.cards.remove(self.cards[0])
        print(c)
        return c
    
    def addWinner(self, cardsWon):
        for card in cardsWon:
            self.add(card)

class WarPlayer(WarStack):
    """A War Player."""
    def isPlaying(self):
        return self.cards
    
    def lose(self):
        print(self.name, "loses.")
    
    def win(self):
        print(self.name, "wins.")
    
    # to add:
    # game condition - when a player has three or les cards in hand, to be able
    # to choose either card in play. it may be a little difficult to implement

class WarGame(object):
    """A War Game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = WarPlayer(name)
            self.players.append(player)
        
        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()
    
    @property
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if player.isPlaying():
                sp.append(player)
        return (len(sp) == 1)
    
    def noWinnerRound(self, topCards):
        # if more than one player has a winning card, return all cards to their origin
        for i in range(len(self.players)):
            self.players[i].add(topCards[i])
    
    def clearPlayers(self):
        # at the end of a round, remove players from the game who have no cards left in their hand
        for player in self.players:
            if not player.isPlaying():
                print(f"{player.name} has no cards left! Removing them from the current game.")
                self.players.remove(player)
    
    def endGame(self):
        print(f"{self.players[0]} has won this game of War. Congratulations!\
                You are the champion of the people!")
    
    def play(self):
        # deal the players some cards
        self.deck.deal(self.players, perHand=54//len(self.players))
        for player in self.players:
            print(player)
        
        print("Let the game begin!")
        
        # game round counter
        self.round = 0
        while self.stillPlaying:
            self.round += 1
            print(f"Round {self.round}:")

            self.topCards = []
            for player in self.players:
                print(player.cards[0])
                self.topCards.append(player.pipCard())
            
            self.topCardNum = 0
            self.topCardWinner = True
            for cardNum in range(len(self.topCards[1:])):
                if self.topCards[self.topCardNum].value < self.topCards[cardNum+1].value:
                    self.topCardNum = cardNum + 1
                    self.topCardWinner = True
                elif self.topCards[self.topCardNum].value == self.topCards[cardNum+1].value:
                    self.topCardWinner = False
            
            if not self.topCardWinner:
                print("No winner this round! Everyone recieves back their cards.")
                self.noWinnerRound(self.topCards)
            else:
                print(f"{self.players[self.topCardNum].name} wins this round.")
                self.players[self.topCardNum].addWinner(self.topCards)
            
            self.clearPlayers()
            if len(self.players) == 1:
                self.endGame()
                break
            input("Press enter for next round...\n")

def main():
    print("\t\tWelcome to War, the simple one-card many-player game!\n")

    names = []
    number = games.askNumber("How many players? (1 - 7):", low=1, high=8)
    for i in range(number):
        name = input("Enter player name: ").capitalize()
        names.append(name)
    
    print()
    
    game = WarGame(names)
    again = None
    while again != "n":
        game.play()
        again = games.askYesNo("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")
