import random


class Card:

    def __init__(self, Value, Suit):
        self.known = False
        self.value = Value
        self.suit = Suit

        if self.suit == "♠" or self.suit == "♣": #sets the colour of the card to black if suite is spades, or clubs
            self.colour = "black"

        elif self.suit == "♥" or self.suit == "♦": #sets the colour of the card to red if the suite is hearts or diamonds
            self.colour = "red"

    def val(self, truenumber): #returns the value itself
        if truenumber == True: #returns the true value of the card
            return self.value
        else:
            if self.value > 10:
                special = ["J", "Q", "K"] # if the card has a value of 11, 12, 13 it returns, jack queen or king
                return special[self.value - 11]
            elif self.value == 1: # if the card has a value of 1 it returns ace
                return "a"
            else:
                return self.value    # if card is over 1 but under 11 i will return the orginal value

    def suite(self): # returns the suite of the card
        return self.suit

    def colour(self): # returns the colour of the card defined at the start if the class
        return self.colour

    def pcolour(self):  # returns the "print" color.
        if self.colour == "black":
            return "\033[0;30;47m"
        if self.colour == "red":
            return "\033[0;31;47m"

    def known(self): #returns wether or not the card is known
        if self.know == True:
            return True
        else:
            return False

    def hide(self):  # makes a True known value False
        self.known = False

    def flip(self): #makes a Flase known value true
        self.known = True


class Deck:

    def __init__(self):
        self.cards = []
        self.basestate = "  "

#creates a full deck of cards
    def create(self):
        for a in ("♦", "♥", "♣", "♠"):
            for i in range(13):
                self.cards.append(Card(i + 1, a))

#shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

#returns a card in a printatble form
    def veiwcard(self, position):
        normal = "\033[0;37;40m" # =varible to make it easier when we want to go back to normal print colour

        if position <= 0:
            if len(self.cards) == 0: #if the deck is empty it returns a "blank car" to show there is a deck there but no card
                temp = "[ " + self.basestate + "  ]"
                return temp

        # if a poistion that is out of the upper bouds of our cards array, it will return a blank space
        if position > len(self.cards) - 1:
            return normal + "       "

        #returns printable card if value is known
        elif self.cards[position].known == True:
            temp = self.cards[position]

        # adds a space to make 9 and 10 the same length
            if temp.val(True) != 10:
                temp = temp.pcolour() +"[ " + temp.suite() + str(temp.val(False)) + "  ]"+ normal
            else:
                temp = temp.pcolour() + "[ " + temp.suite() + str(temp.val(False)) + " ]" +normal
            return temp

        #The card is unkown it will return a back of a card
        else:
            return normal + "\033[0;27;44m"+"[ xxx ]"+normal

#returns a card class and removing it from the deck
    def getcard(self, position):

        if position > len(self.cards): #checks the position is within the array, if not it returns nothing
            return " "
        else: #if positinon is within the array of cards, it returns the card in that position then removes from cards array
            temp = self.cards[position]
            self.cards.pop(position)
            return temp

#returns a card class without removing it from the deck
    def get(self, position):
        return self.cards[position]

#adds a card to the cards array
    def add(self, card):
        self.cards.append(card)
        return ()

#returns the legnth of the cards array
    def getl(self):
        return len(self.cards)

#tells the top card of the deck to make its known value True
    def flip(self):
        self.cards[len(self.cards) - 1].flip()

#displays board
def displayboard():
    normal = "\033[0;37;40m" #sets normal print colour

    # printing off foundation numbering
    for i in range(28):
        print(" ", end='')
    for i in range(4):
        print("   ", i + 1, "   ", end='')
    print("")

    # prints off top row
    print("  ", drawdeck.veiwcard(0),normal, end=' ')
    print(discardeck.veiwcard(discardeck.getl() - 1),normal, "         ", end='')
    for i in range(len(foundations)):
        print(foundations[i].veiwcard(foundations[i].getl()-1),normal, end=' ')
    print("")
    print(" ", end='')

    # printing off lettering of the 7 piles
    print(" ", end='')
    for i in ("A", "B", "C", "D", "E", "F", "G"):
        print("   ", i, "   ", end="")
    print("")
    for i in range(findmax()):
        if i >= 9:
            temp = i +1
        else:
            temp = str(i + 1) + " "

        print(temp, end='')  # left side numbers
        for a in range(7):
            print("",board[a].veiwcard(i), end=' ')
        print(" ", i + 1)  # right side numbers

#tells all the decks in the board array to change to top card's known value to true
def fliptop():
    for i in range(7):
        if board[i].getl() > 0:
            board[i].flip()

#creates the array of decks it uses and sets the cards up in the correct order
def createboard():
    for i in range(7):  # populates the Board array with our decks
        board.append(Deck())
    drawdeck.create()  # creates a full deck in our draw deck
    # drawdeck.shuffle()  #shuffles draw deck

    for i in range(7):  # creates Tableau
        for b in range(7):  # populates the card
            if b >= i:
                board[b].add(drawdeck.getcard(0))
    for i in ("♦", "♥", "♣", "♠"): # creates foundations
        foundations.append(Deck())

#checks two cards to see if putting one on top another is a legal move
def legal(first, placing):
    if first.colour != placing.colour:
        if first.val(True) == placing.val(True) + 1:
            return True
        else:
            return False


def addfoundation(card):
    if card.val(True) == 1:  # checks to see if it is an ace
        for i in range(len(foundations)):  # goes through all foundations
            if foundations[i - 1].getl() == 0:  # checks to see if foundations are empty
                foundations[i - 1].add(card)  # if foundation is empty, it populates it with the card
                return True
    else:
        for i in range(len(foundations)):  # checks all the foundations
            if foundations[i - 1].getl() > 0:  # sees if they are populated
                if foundations[i - 1].get(foundations[i - 1].getl()-1).suite() == card.suite():  # if populated checks to see if its the same suite
                    if foundations[i - 1].get(foundations[i-1].getl()-1).val(True)+1 == card.val(True):# checks if the card is the a value above the card alreay in the foundation deck
                        foundations[i - 1].add(card)
                        return True
        return False



def getinput():
    userinpt = input("\nplease select the pile you want to pick up from (A,B,C,D,E,F,G)\nor entre \n1) Draw\n2) Pickup from draw pile\n3) Pick up from foundations\n").upper()
    a = 0

    # draws a card from the draw deck to the discard deck
    if userinpt == "1":
        if drawdeck.getl() == 0: #if there are no cards if the draw deck it takes all the cards from the discard deck and puts it into the draw deck
            for i in range(discardeck.getl()):
                discardeck.get(0).hide()
                drawdeck.add(discardeck.getcard(0))
            return
        discardeck.add(drawdeck.getcard(0))
        discardeck.flip()
        return

    #takes a card from the top of the discard deck
    if userinpt == "2":

        if discardeck.getl() == 0: #returns an error if there is nothing in the discardeck
            clear()
            error("enter to continue")
            return

        print(discardeck.veiwcard(discardeck.getl() - 1)) #displays the card so the player is sure of what they are moving

        userinpt = input("\nselect the pile you want to place it on (A,B,C,D,E,F,G)\nor\n1) Place into foundations\n").upper()
        a = 0
        if userinpt == "1": # if the user wants to put it into the foundation decks
            if addfoundation(discardeck.get(discardeck.getl() - 1)) == True:
                discardeck.getcard(discardeck.getl() - 1)
                return
        else:
            for i in ("A", "B", "C", "D", "E", "F", "G"):# it the user want to put the card onto the board
                a += 1
                if userinpt == i:
                    z = a
                    a = True
                    break
            if a != True:
                error("please input a valid input")
                return


            if board[z-1].getl() == 0: # if the deck in the board refrenced is empty, it makes sure that a king will populate it first
                if discardeck.get(discardeck.getl()-1).val(True) == 13:
                    board[z-1].add(discardeck.getcard(discardeck.getl() - 1))
                    return
            elif legal(board[z-1].get(board[z-1].getl()-1), discardeck.get(discardeck.getl() - 1)) == True: #checks if the move is legal
                board[z-1].add(discardeck.getcard(discardeck.getl() - 1))
                return
            else:
                error("not a legal move")
                return

#takes a card from the founation decks
    if userinpt == "3":
        userinpt = input("what foundation do you want to get a card from, 1,2,3,4")
        x = 0
        for i in ("1", "2", "3", "4"):
            x += 1
            if userinpt == i:

                if foundations[x - 1].getl() > 0:
                    print(foundations[x - 1].veiwcard(foundations[x - 1].getl() - 1))
                    userinpt = input("select the pile you want to place it on (A,B,C,D,E,F,G\n").upper()
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
                        if board[z-1].getl() == 0:
                            if foundations[x-1].get(foundations[x-1].getl()-1).val(True) == 13:
                                board[z - 1].add(foundations[x - 1].getcard(foundations[x - 1].getl() - 1))
                            else:
                                error("can only place king there")
                                return
                        else:
                            if legal(board[z - 1].get(board[z - 1].getl() - 1),foundations[x - 1].get(foundations[x - 1].getl() - 1)) == True:
                                board[z - 1].add(foundations[x - 1].getcard(foundations[x - 1].getl() - 1))
                                return
                            else:
                                error("this is not a legal move")
                                return
                            return

    for i in ("A", "B", "C", "D", "E", "F", "G"):
        a += 1
        if userinpt == i:
            x = a
            a = True  # lets us know that the answer has been found
            break
    if a != True:  # if the input is not valid, tells the user and starts back from the start
        error("please input a valid input")
        return

    try:  # if anything goes wrong, it will get the user to start again, as the input was not valid
        print("please select the card from 1 -", board[x - 1].getl())
        userinpt = input()
        for i in range(findmax() + 1):
            if userinpt == str(i):
                if board[x - 1].getl() < i:
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

    userinpt = input(
        "select the pile you want to place it on (A,B,C,D,E,F,G) \nor\n1) Place into foundations\n").upper()
    a = 0

    if userinpt == "1":  # places into foundation
        if board[x-1].getl() == y:
            if addfoundation(board[x - 1].get(y - 1)) == True:
                board[x-1].getcard(y-1)
                return
            else:
                error("cannot move into foundations") #if you canot place into foundations it will
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
        if board[z - 1].getl() == 0:  # checks to see if pile card is going is empty
            if board[x - 1].get(y - 1).val(True) == 13:  # checks to see if card moving is a king
                board[z - 1].add(board[x - 1].getcard(y - 1))  # if all above is true, places
                return
            else:  # if you are trying to something that is not a king, it tell the user they cant
                error("You can only move a king here")
                return

        # if you are moving a card ontop of another card, it will check if its legal then moves the card. if the move is not legal it will inform the user
        if legal(board[z - 1].get(board[z - 1].getl() - 1),board[x - 1].get(y - 1)) == True:
            board[z - 1].add(board[x - 1].getcard(y - 1))
            try:
                while True:
                    board[z - 1].add(board[x - 1].getcard(y - 1))
            except:
                return
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


drawdeck = Deck()  # creates the draw, discard decks
discardeck = Deck()
hand = Deck()
board = []
foundations = []
rungame()
