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
        self.boardMatrix = numpy.zeros((rows, columns))

    """
    Attempts to add a piece to a certain column. If the column is 
    full the move is illegal and false is returned, otherwise true 
    is returned.
    """
    def addPiece(self, column, value):
        "Check if column is full."
        if self.boardMatrix.item(0,column) != 0:
            return False

        "Place piece."
        for y in range(self.rows):
            currentValue = self.boardMatrix.item(y, column)

            if currentValue == 0:
                if y == self.rows - 1:
                    self.boardMatrix.itemset((y, column), value)                    
                else:
                    continue                
        return True
