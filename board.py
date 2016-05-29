import numpy, random

"""
Board represents a four in a row game board.

Author: Isaac Arvestad
"""
class Board:
    """
    Initializes the game with a certain number of rows
    and columns.
    """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = numpy.zeros((rows, columns))

    """
    Attempts to add a piece to a certain column. If the column is 
    full the move is illegal and false is returned, otherwise true 
    is returned.
    """
    def add_piece(self, column, value):
        "Check if column is full."
        if self.matrix.item(0,column) != 0:
            return False

        "Place piece."
        for y in range(self.rows):
            if y == self.rows - 1: # Reached bottom
                self.matrix.itemset((y, column), value)
                break
            elif self.matrix.item(y + 1, column) == 0: # Next row is also empty
                continue
            else: # Next row is not empty
                self.matrix.itemset((y, column), value)
                break
        return True

    """
    Returns the column which the ai want to place their piece in.
    Column is 0 indexed. Returns -1 if no moves are available.
    """
    def get_ai_move(self):
        available_moves = []
        for i in range(self.columns):
            if self.matrix.item(0,i) == 0:
                available_moves.append(i)
        if len(available_moves) == 0:
            return -1

        index = random.randint(0, len(available_moves)-1)
        return available_moves[index]

    """
    Evaluates the board position and checks if a player has won, a draw
    has occured or if the game if unfinished. Does not check if both 
    players have four in a row as it is assumed that the board is 
    evaluated every move.

    Returns an interger where:
    0 = unfinished
    1 = player 1 won
    2 = player 2 won
    -1 = draw
    """
    def evaluate_board(self):
        # Check for win
        for x in range(self.columns):
            for y in range(self.rows):
                initial_piece = self.matrix.item((y,x))
                if initial_piece == 0:
                    continue
                for i in range(0,8):
                    (dx, dy) = self.get_dx_dy(i)
                    for j in range(1,4):
                        next_x = x + dx*j
                        next_y = y + dy*j
                        if self.coordinates_within_bounds(next_x, next_y) == True:
                            next_piece = self.matrix.item((next_y, next_x))
                            if next_piece != initial_piece:
                                break
                            if j == 3:
                                return initial_piece
        
        # Check for draw
        for x in range(self.columns):
            if self.matrix.item((0,x)) == 0:
                return 0
        return -1

    """
    Helper method which returns the step in x and y directions for the evaluate_board
    algorithm. If index is outside of the 8 possible directions [0,7] nothing is 
    returned.
    """
    def get_dx_dy(self, index):
        if index == 0: return (1, 0)
        elif index == 1: return (1, 1)
        elif index == 2: return (0, 1)
        elif index == 3: return (-1, 1)
        elif index == 4: return (-1, 0)
        elif index == 5: return (-1, -1)
        elif index == 6: return (0, -1)
        elif index == 7: return (1, -1)

    """
    Returns true if coordinates are within bounds, false if they are not.
    """
    def coordinates_within_bounds(self, column, row):
        if column < 0 or column > self.columns - 1 or row < 0 or row > self.rows - 1:
            return False
        return True
