# Blackjack
# From 1 to 7 players compete against a dealer

import cards, games

class BJCard(cards.Card):
    """ A Blackjack card."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.isFaceUp:
            v = BJCard.RANKS.index(self.rank)+1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJDeck(cards.Deck):
    """A Blackjack Deck."""
    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))

class BJHand(cards.Hand):
    """A Blackjack Hand."""
    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ":\t" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    
    @property
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value
        
        # determine if hand contains an Ace
        containsAce = False
        for card in self.cards:
            if card.value == BJCard.ACE_VALUE:
                containsAce = True
        
        # if hand contains Ace and total is low enough, treat Ace as 11
        if containsAce and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10
        
        return t
    
    def isBusted(self):
        return self.total > 21

class BJPlayer(BJHand):
    """A Blackjack Player."""
    def isHitting(self):
        response = games.askYesNo("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"
    
    def bust(self):
        print(self.name, "busts")
        self.lose()
    
    def lose(self):
        print(self.name, "loses.")
    
    def win(self):
        print(self.name, "wins.")
    
    def push(self):
        print(self.name, "pushes.")

class BJDealer(BJHand):
    """A Blackjack Dealer."""
    def isHitting(self):
        return self.total < 17
    
    def bust(self):
        print(self.name, "busts.")
    
    def flipFirstCard(self):
        firstCard = self.cards[0]
        firstCard.flip()

class BJGame(object):
    """A Blackjack Game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJPlayer(name)
            self.players.append(player)
        
        self.dealer = BJDealer("Dealer")

        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()
    
    @property
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp
    
    def __additionalCards(self, player):
        while not player.isBusted() and player.isHitting():
            self.deck.deal([player])
            print(player)
            if player.isBusted():
                player.bust()
    
    def play(self):
        # deal initial 2 cards each
        self.deck.deal(self.players + [self.dealer], perHand = 2)
        self.dealer.flipFirstCard()     # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additionalCards(player)
        
        self.dealer.flipFirstCard()     # reveal dealer's first card

        if not self.stillPlaying:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additionalCards(self.dealer)

            if self.dealer.isBusted():
                # everyone still playing wins
                for player in self.stillPlaying:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.stillPlaying:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        
        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tWelcome to Blackjack!\n")
    
    names = []
    number = games.askNumber("How many players? (1 - 7):", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ").capitalize()
        names.append(name)
    
    print()

    game = BJGame(names)
    
    again = None
    while again != "n":
        game.play()
        again = games.askYesNo("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")