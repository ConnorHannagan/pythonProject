import random
class Card:

    def __init__(self, Value, Suit):
        self.known = False
        self.value = Value
        self.suit = Suit
        if self.suit == "♠" or self.suit == "♣":
            self.colour = "black"
        elif self.suit == "♥" or self.suit == "♦":
            self.colour = "red"

    def val(self,truenumber):
        if truenumber == True:
            return self.value
        else:
            if self.value > 10:
                special = ["J","Q","K"]
                return special[self.value-11]
            elif self.value == 1:
                return "a"
            else:
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

    def __init__(self, base):
        self.cards = []
        self.basestate = base

    def create(self):
        for a in ("♦", "♥", "♣", "♠"):
            for i in range(13):
                self.cards.append(Card(i+1, a))

    def shuffle(self):
        random.shuffle(self.cards)

    def veiwcard(self,position):
        if position == 0:
            if len(self.cards) == 0:
                temp = "[" + self.basestate + "  ] "
                return temp

        if position > len(self.cards)-1:
            return "        "

        elif self.cards[position].known == True:
                temp = self.cards[position]
                if temp.val(True) != 10:
                    temp = " [ " + temp.suite() + str(temp.val(False)) + "  ]"
                else:
                    temp = " [ " + temp.suite() + str(temp.val(False)) + " ]"
                return temp
        else:
            return " [ xxx ]"

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
            print(i.value(False), i.suit(), i.colour())

    def getl(self):
        return len(self.cards)

    def flip(self):
        self.cards[len(self.cards)-1].flip()


def displayboard():
    print("", drawdeck.veiwcard(0), discardeck.veiwcard(0), "       ", end= '')
    for i in range(len(foundations)):
        print(foundations[i].veiwcard(0), end='')
    print("")
    print(" ", end ='')
    for i in ("A","B","C","D","E","F","G"):
        print ("   ", i, "  ", end = "")
    print("")
    for i in range(7):
        print(i+1, end= '') #left side numbers
        for a in range(7):
            print(board[a].veiwcard(i), end='')
        print(" ",i+1) #right side numbers

def fliptop():
    for i in range(7):
        if board[i].getl() > 0:
            board[i].flip()

def createboard():


    for i in range(7): #populates the Board array with our decks
        board.append(Deck("      "))

    drawdeck.create()  #creates a full deck in our draw deck
    drawdeck.shuffle()  #shuffles draw deck

    for i in range(7): # creates Tableau
        for b in range(7):  # populates the card
            if b >= i:
                board[b].add(drawdeck.getcard(0))
    for i in ("♦", "♥", "♣", "♠"):
        foundations.append(Deck(" " + i + " "))

def getinput():
    userinpt = input("please select the pile you want to pick up from (A,B,C,D,E,F,G)\n").upper()
    a = 0
    for i in ("A", "B", "C", "D", "E", "F", "G"):
        a += 1
        if userinpt == i:
            x = a
    userinpt = input("please select the card from 1 - 7 ")
    for i in range(7):
        if userinpt == str(i):
            y = i
    print(board[x - 1].veiwcard(y - 1))
    userinpt = input("select the pile you want to place it on (A,B,C,D,E,F,G)").upper()
    a = 0
    for i in ("A", "B", "C", "D", "E", "F", "G"):
        a += 1
        if userinpt == i:
            z = a
    board[z - 1].add(board[x - 1].getcard(y - 1))

def rungame():
    createboard()
    while True:
        fliptop()
        displayboard()
        getinput()




def findmax():
    max = 0
    for i in range(7):
        if board[i].getl() > max:
            max = board[i].getl()
    return max




drawdeck = Deck("   ") #creates the draw, discard decks
discardeck = Deck("   ")
board = []
foundations = []
rungame()

