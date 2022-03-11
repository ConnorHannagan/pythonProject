
class game:
    def __init__(self, playerx, playery, turn):
        self.playerx = int(playerx)
        self.playery = int(playery)
        self.turn = 1
    #
    #


    def insert(self):
        if board[self.playerx-1][self.playery-1] == " - ":
            if self.turn == 1:
                board[self.playerx-1][self.playery-1] = " x "
                self.turn = 2
            elif self.turn == 2:
                board[self.playerx-1][self.playery-1] = " o "
                self.turn = 1
            else:
                print("trun error")
        else:
            print("please enter an empty space")

    def disboard(self):
        print("   1 ", " 2 ", " 3 ")
        for i in range(len(board)):
            print( i +1, board[i][0], board[i][1], board[i][2])

    def checkwin(self):
        print("okay sure")
        games.checkx

    def checkx(self):
        for i in range(len(board)):
            print("w")
            for a in range(len(board[i]), len(board[i]-1)):
                if board[i][a] == board[i][i+1]:
                    print('yasss')



board = []
for i in range(3):
    across = []
    for a in range(3):
        across.append(" - ")
    board.append(across)

games = game("1", "1", 1)
while True:
    games.disboard()

    try:
        games.playerx = int(input("please enter across coordinates : "))
        games.playerx = int(input("please input vertical coordinates : "))
        games.insert()

    except:
        input("please enter 1, 2 or 3")
    games.checkwin()