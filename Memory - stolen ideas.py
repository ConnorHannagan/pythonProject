import random
class Card:
    def __init__(self, Number, Known):
        self.number = Number
        self.known = Known

    def show(self):
        if self.known == False:
            print(self.number)
        elif self.known == True:
            print("-")

class Deck:
    def __init__(self):
        self.cardall = []
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def getval(self, x):
        return self.cards[x]

    def createdeck(self):
        for i in range(4):
            for a in range(13):
                self.cards.append(Card(a+1, False))
        return

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def show(self):
        for s in self.cardall:
            s.show()

    def taketop(self):
        try:
            self.topcard = self.cards[0]
            self.cards.pop(0)
            return self.topcard
        except:
            return False


temp = Deck()
temp.createdeck()
temp.shuffle()
temp.show()