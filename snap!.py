import random
class card:
   def  __init__(self, suit, number):
       self.suit = suit
       self.number = number

   def show(self):
        print(self.number,"of",self.suit)

   def checkval(self):
       return self.number






class Deck:
    def __init__(self):
        self.cards = []
        self.topcard = ""

    def add(self, card):
            self.cards.insert(0, card)

    def createdeck(self):
        for i in ("Diamonds", "Hearts", "Spades", "Clubs"):
            for a in range(13):
                self.cards.append(card(i, a+1))

    def show(self):
        for s in self.cards:
            s.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def taketop(self):
        try:
            self.topcard = self.cards[0]
            self.cards.pop(0)
            return self.topcard
        except:
            return False

    def checktop(self, id):
        return self.cards[id]

    def checkwin(self):
        if(len(self.cards) <=1):
            return False
        if self.cards[1].checkval() == self.cards[0].checkval():
            input()
            print("SNAPPPPPP")
            while True:
                userinpt = input("who won?\n1) player 1\n2) player 2\n")
                if userinpt == "1" or userinpt == "2":
                    return userinpt
                else:
                    print("please enter 1 or 2 ")
        return False

    def legnth(self):
        return len(self.cards)

deck = Deck()
deck.createdeck()
deck.shuffle()
player1 = Deck()
player2 = Deck()
for i in range(26): #splits deck into 2 decks for the players
    player1.add(deck.taketop())
    player2.add(deck.taketop())

turn  = 1
won = False
while True: #contains the game
    for i in range(26): #lets game have 26 go's each round
        input()


        if turn == 1: #if its player 1's turn
            if player1.legnth() == 0: #checks if the player has cards left to put down
                won = True
                break
            deck.add(player1.taketop())
            deck.checktop(0).show()
            if deck.checkwin() != False:
                break
            turn = 2
        elif turn == 2:#if its player 2's turn
            if player2.legnth() == 0: #checks if the player has cards left to put down
                won = True
                break

            deck.add(player2.taketop())
            deck.checktop(0).show()
            if deck.checkwin() != False:
                break
            turn = 1


    print(deck.checkwin())
    if deck.checkwin() == "1":
        if won == False:
            for i in range(deck.legnth()):
                player1.add(deck.taketop())

    elif deck.checkwin() == "2":
        if won == False:
            for i in range(deck.legnth()):
                player2.add(deck.taketop())


    print(player1.legnth())
    print("---------------")
    print(player2.legnth())





