import random
class Card:

    def __init__(self, Value, Suit):
        self.known = False
        self.value = Value
        self.suit = Suit
        if self.suit == "S" or self.suit == "C":
            self.colour = "black"
        elif self.suit == "H" or self.suit ==  "D":
            self.colour = "red"


    def val(self):
        return self.value

    def suite(self):
        return self.suit

    def colour(self):
        return self.colour

    def known(self):
        return self.known

    def flip(self):
        self.known = True


class Deck:

    def __init__(self):
        self.cards = []


    def create(self):
        for a in ("D", "H", "C", "S"):
            for i in range(13):
                self.cards.append(Card(i+1, a))

    def shuffle(self):
        random.shuffle(self.cards)

    def veiwcard(self,position):
        if position > len(self.cards)-1:
            return "        "
        elif self.cards[position].known == True:
                temp = self.cards[position]

                if temp.val() < 10:
                    temp = " [ " + temp.suite() + str(temp.val()) + "  ]"
                else:
                    temp = " [ " + temp.suite() + str(temp.val()) + " ]"
                return temp
        else:
            return " [     ]"

    def getcard(self, position):
        if position > len(self.cards):
            return " "
        else:
            temp = self.cards[position]
            self.cards.pop(position)
            return temp
        # if position == 0:
        #     return position.self.cards
        # if position > 0:
        #     if position.self.cards.known == False:
        #         return False
        #     else:
        #         return position.self.cards

    def add(self, card):
        self.cards.append(card)
        return()

    def print(self):
        for i in self.cards:
            print(i.value(), i.suit(), i.colour())

    def getl(self):
        return len(self.cards)

    def flip(self):
        self.cards[len(self.cards)-1].flip()


def displayboard():
    for i  in range(7):
        print(board[0].veiwcard(i),board[1].veiwcard(i),board[2].veiwcard(i),board[3].veiwcard(i),board[4].veiwcard(i),board[5].veiwcard(i), board[6].veiwcard(i))

def fliptop():
    for i in range(7):
        board[i].flip()


create board
drawdeck = Deck()
drawdeck.create()
discardeck = Deck()
board = []
drawdeck.shuffle()
for i in range(7):
    board.append(Deck())
for i in range(7):
    for b in range(7): #creates 7 decks to start off with
        if b >= i:
            board[b].add(drawdeck.getcard(0))




