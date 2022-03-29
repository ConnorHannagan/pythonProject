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
    def veiwcard(self,position):
        if position > len(self.cards)-1:
            return " "
        else:
            temp = self.cards[position]
            if temp.val() < 10:
                temp = "0" + str(temp.val())
            else:
                temp = temp.val()
            return temp

    def getcard(self, position):
        if position > len(self.cards):
            return " "
        else:
            temp = self.cards[position]
            self.cards.pop(0)
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

drawdeck = Deck()
drawdeck.create()
discardeck = Deck()
board = []
for i in range(7):
    board.append(Deck())
for i in range(7):
    for b in range(7): #creates 7 decks to start off with
        if b >= i:
            board[b].add(drawdeck.getcard(0))


for i in range(7):
    print(board[0].veiwcard(i),board[1].veiwcard(i),board[2].veiwcard(i),board[3].veiwcard(i),board[4].veiwcard(i),board[5].veiwcard(i), board[6].veiwcard(i))




# for i in range(7):
#     row = []
#     for a in range(7):
#         temp = board[a].getcard(i-1)
#         if temp == " ":
#             row.append("")
#         else:
#             row.append(temp.val())
#     print(row)


