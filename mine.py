class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if self.suit == "S" or self.suit == "C":
            self.colour = "black"
        elif self.suit == "H" or self.suit == "D":
            self.colour = "red"



    def getval(self):
        return self.value
    def getsuit(self):
        return self.suit
    def getcolour(self):
        return self.colour

class Deck:
    def __init__(self):
        self.cards = []
    def create(self):
        for a in ("D", "H", "C", "S"):
            for i in range(13):
                self.cards.append(Card(i+1, a))

    def print(self):
        for i in self.cards:
            print(i.getval(), i.getsuit(),i.getcolour())

game = Deck()
game.create()
game.print()
