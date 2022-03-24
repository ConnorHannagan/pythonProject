import random
class Card:
    def __init__(self, value, suit):
        self.known = False
        self.value = value
        self.suit = suit
        if self.suit == "S" or "C":
            self.colour = "black"
        elif self.suit == "H" or "D":
            self.colour = "red"
    def val(self):
        return self.value
    def suit(self):
        return self.suit
    def colour(self):
        return self.colour
    def known(self):
        return self.known

class Deck:
    def __init__(self):
        self.cards = []
    def create(self):
        for a in ("D", "H", "C", "S"):
            for i in range(13):
                self.cards.append(Card(i+1, a))
    def shuffle(self):
        random.shuffle(self.cards)
    def getcard(self, position):
        if position == 1:
            return position.self.cards
        if position > 1:
            if position.self.cards.known == False:
                return False
            else:
                return position.self.cards

    def print(self):
        for i in self.cards:
            print(i.value(), i.suit(), i.colour())


drawdeck = Deck()
drawdeck.create()
discardeck = Deck()
board = []
for i in range(7):
    board.append(Deck())
for i in range(7):
    for b in range(7):


print(drawdeck.getcard(1).val)
