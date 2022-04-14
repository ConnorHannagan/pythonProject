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
        if self.know == True:
            return True
        else:
            return False

    def hide(self):
        self.known = False

    def flip(self):
        self.known = True

class Deck:

    def __init__(self):
        self.cards = []
        self.basestate = "     "

    def create(self):
        for a in ("♦", "♥", "♣", "♠"):
            for i in range(13):
                self.cards.append(Card(i+1, a))

    def shuffle(self):
        random.shuffle(self.cards)

    def veiwcard(self,position):
        if position <= 0:
            if len(self.cards) == 0:
                temp = "[" + self.basestate + "] "
                return temp

        if position > len(self.cards)-1:
            return "         "

        elif self.cards[position].known == True:
                temp = self.cards[position]
                if temp.val(True) != 10:
                    temp = " [ " + temp.suite() + str(temp.val(False)) + "  ] "
                else:
                    temp = " [ " + temp.suite() + str(temp.val(False)) + " ] "
                return temp
        else:
            return " [ xxx ] "

    def getcard(self, position):
        if position > len(self.cards):
            return " "
        else:
            temp = self.cards[position]
            self.cards.pop(position)
            return temp

    def get(self, position):
        return self.cards[position]

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
    print("", drawdeck.veiwcard(0), discardeck.veiwcard(discardeck.getl()-1), "         ", end= '')
    for i in range(len(foundations)):
        print(foundations[i].veiwcard(0),"", end='')
    print("")
    print(" ", end ='')
    for i in ("A","B","C","D","E","F","G"):
        print ("   ", i, "   ", end = "")
    print("")
    for i in range(findmax()):
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
        board.append(Deck())

    drawdeck.create()  #creates a full deck in our draw deck
    # drawdeck.shuffle()  #shuffles draw deck

    for i in range(7): # creates Tableau
        for b in range(7):  # populates the card
            if b >= i:
                board[b].add(drawdeck.getcard(0))
    for i in ("♦", "♥", "♣", "♠"):
        foundations.append(Deck())

def getinput():
    userinpt = input("please select the pile you want to pick up from (A,B,C,D,E,F,G)\n\nor\n1) Draw\n2) Pickup from draw pile\n3) Pick up from foundations\n").upper()
    a = 0
    if userinpt == "1":
        if drawdeck.getl() == 0:
            for i in range(discardeck.getl()):
                discardeck.get(0).hide()
                drawdeck.add(discardeck.getcard(0))
            return
        discardeck.add(drawdeck.getcard(0))
        discardeck.flip()
        return

    if userinpt == "2":

        if discardeck.getl() == 0:
            clear()
            input("draw deck is empty \n\n\nenter to continue")
            return
        print(discardeck.veiwcard(discardeck.getl()-1))
        userinpt = input("select the pile you want to place it on (A,B,C,D,E,F,G)").upper()
        a = 0

        for i in ("A", "B", "C", "D", "E", "F", "G"):
            a += 1
            if userinpt == i:
                z = a
                a = True
                break
        if a != True:
            error("please input a A,B,C,D,E,F,G")
            return
        board[z-1].add(discardeck.getcard(discardeck.getl()-1))
        return


    for i in ("A", "B", "C", "D", "E", "F", "G"):
        a += 1
        if userinpt == i:
            x = a
            a = True #lets us know that the answer has been found
            break
    if a != True: #if the input is not valid, tells the user and starts back from the start
        error("please input a valid input")
        return


    try: # if anything goes wrong, it will get the user to start again, as the input was not valid
        print("please select the card from 1 -", board[x-1].getl())
        userinpt = input()
        for i in range(findmax()+1):
            if userinpt == str(i):
                if board[x-1].getl() < i:
                    error("please input a card that exists")
                    return
                else:
                    if board[x - 1].get(i - 1).known == True:
                        y = i
                    else:
                        error("please input a known card")
                        return
        print(board[x - 1].veiwcard(y - 1))
    except:
        error("please input a card that exists")
        return

    userinpt = input("select the pile you want to place it on (A,B,C,D,E,F,G) \nor\n1) Place into foundations\n").upper()
    a = 0


    if userinpt == "1":

        if board[x-1].get(y-1).val(True) == 1: #checks to see if it is an ace
            for i in range(len(foundations)): #goes through all foundations
                if foundations[i - 1].getl() == 0: #checks to see if foundations are empty
                    foundations[i-1].add(board[x-1].getcard(y-1)) #if foundation is empty, it populates it with the card
                    return
        else: # if the card is not an ace it will return an error for the user to do another move
            error("")
            return

        for i in range(len(foundations)): #checks all the foundations
            if foundations[i-1].getl() > 0: #sees if they are populated
                if foundations[i-1].get(foundations[i-1].getl()).suite == board[x-1].get(y-1): # if populated checks to see if its the same suite
                    foundations[i-1].add(board[x-1].getcard(y-1))
                    return

    for i in ("A", "B", "C", "D", "E", "F", "G"):
        a += 1
        if userinpt == i:
            z = a
            a = True
            break
    if a != True:
        error("please input a A,B,C,D,E,F,G")
        return
    else:
        if board[x - 1].get(y - 1).colour != board[z-1].get(board[z-1].getl()-1).colour:
            if board[z-1].get(board[z-1].getl()-1).val(True) - 1 == board[x - 1].get(y - 1).val(True):
                board[z - 1].add(board[x - 1].getcard(y - 1))
        else:
            error("this is not a legal move")
            return

def rungame():
    createboard()
    while True:
        fliptop()
        displayboard()
        getinput()

def error(error):
    clear()
    temp = error + "\n\n\nenter to continue"
    input(temp)

def clear():
    for i in range(20):
        print("")

def findmax():
    max = 0
    for i in range(7):
        if board[i].getl() > max:
            max = board[i].getl()
    return max


drawdeck = Deck() #creates the draw, discard decks
discardeck = Deck()
hand = Deck()
board = []
foundations = []
rungame()

