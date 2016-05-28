import numpy

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
