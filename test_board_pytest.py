from board import Board

def test_constructor():
    board = Board(0,0)
    assert board.boardMatrix.size == 0
    assert board.columns == 0
    assert board.rows == 0

    board = Board(5,5)
    assert board.boardMatrix.size == 25
    assert board.columns == 5
    assert board.rows == 5

"""
Tests that one can add pieces to the board and 
that the stack correctly.
"""
def test_addPiece():
    board = Board(5,5)
    assert board.addPiece(0, 1) == True
    assert board.boardMatrix.item((4,0)) == 1

    assert board.addPiece(0, 1) == True
    assert board.boardMatrix.item((3,0)) == 1

    assert board.addPiece(1, 1) == True
    assert board.boardMatrix.item((4,1)) == 1

    assert board.addPiece(4, 1) == True
    assert board.boardMatrix.item((4,4)) == 1

"""
Tests that the board can be filled up completely 
but no more.
"""
def test_addPieceMaxColumn():
    board = Board(5,5)

    # Fill board
    for x in range(board.columns):
        for y in range(board.rows):
            assert board.addPiece(x, 1) == True

    # Attempt to overfill
    for x in range(board.columns):
        assert board.addPiece(x, 2) == False

    # Make sure initially filled values weren't overriden
    for x in range(board.columns):
        for y in range(board.rows):
            assert board.boardMatrix.item((x,y)) == 1
