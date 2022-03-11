import random


# Create the board object
class Board:
    # When we create a board it should know some stuff about itself
    # the board knows how big it is in both dimensions
    def __init__(self, size_x, size_y):
        # It randomly assigns who will play first
        self.players_turn = random.randint(1, 2)
        # Says that the game is not over
        self.over = "None"
        # It creates the playing board
        self.board = []
        for i in range(size_y):
            row = []
            for q in range(size_x):
                # It creates a point within the array
                row.append(Point())
            self.board.append(row)

    # Run game is the part of the board that controls everything
    def run_game(self):
        # It is a loop that first does the players turn, then displays the board, then checks if the game is over
        game.display()
        while self.over == "None":
            game.turn()
            game.display()
            self.over = game.check_controller()

    # turn manages everything related to user input and everything that happens on a players turn
    def turn(self):
        while True:
            x_loc = int(input("enter in your x location "))
            y_loc = int(input("enter in your y location "))
            # If the user is trying to enter into a position that already is being used tell them.
            if self.board[x_loc][y_loc].get_value() != " ":
                print("There is something already there")
            else:
                break
        # Once the player has entered in their location we change the Point at that location and change the turn
        if self.players_turn == 1:
            self.board[x_loc][y_loc].set_value("X")
            self.players_turn = 2
        else:
            self.board[x_loc][y_loc].set_value("O")
            self.players_turn = 1

    # display will create a list of all the values in a row then print out the list
    def display(self):
        for y in range(len(self.board)):
            row = []
            for x in range(len(self.board[y])):
                row.append(self.board[y][x].get_value())
            print(row)

    # Check_controller will run the 4 checks related to a win
    def check_controller(self):
        # I make a copy of the game board
        board = self.board
        outcome = game.check_row(board)
        # Rotates the board to check for a win in a column or an opposite diagonal win
        rotate = list(zip(*board[::-1]))
        if outcome == "None":
            outcome = game.check_row(rotate)
        if outcome == "None":
            outcome = game.check_diagonally(board)
        if outcome == "None":
            outcome = game.check_diagonally(rotate)
        return outcome

    # These methods are static because they don't require self, they only require the board and various outcomes
    def check_row(self, board_type):
        outcome = "None"
        for x in range(len(board_type)):
            # Creates a list made up of a row
            check_list = []
            for y in range(len(board_type)):
                check_list.append(board_type[x][y].get_value())
            # Pass the list to a function that checks if the game has been won
            outcome = game.check_win(check_list)
            if outcome != "None":
                break
        return outcome

    def check_diagonally(self, board_type):
        check_list = []
        outcome = "None"
        for y in range(len(board_type)):
            check_list.append(board_type[y][y].get_value())
        outcome = game.check_win(check_list)
        return outcome

    def check_win(self, l):
        # Check if the space has an x or an o
        if l[0] == "X" or l[0] == "O":
            # Checks if everything in a row is the same
            s = True
            for i in range(len(l)):
                if l[0] != l[i]:
                    s = False
                # Return the winner of the game
            if s == True:
                return l[0]
            else:
                return "None"
        return "None"


# A point is an object that only has a value. This value can be changed or checked
# By default this point has nothing in it
class Point:
    def __init__(self):
        self.value = " "

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


# Create the board
game = Board(2,2)
# Run the game
game.run_game()
print("hello")