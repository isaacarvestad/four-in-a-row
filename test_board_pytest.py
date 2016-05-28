from board import Board

"""
Tests that board matrix is correct size and
that columns and rows are the correct values
when initially constructed. Also tests that
all elements are zero.
"""
def test_constructor():
    board = Board(0,0)
    assert board.matrix.size == 0
    assert board.columns == 0
    assert board.rows == 0

    board = Board(5,5)
    assert board.matrix.size == 25
    assert board.columns == 5
    assert board.rows == 5

    for x in range(board.columns):
        for y in range(board.rows):
            assert board.matrix.item((x,y)) == 0

"""
Tests that one can add pieces to the board and 
that the stack correctly.
"""
def test_add_piece():
    board = Board(5,5)
    assert board.add_piece(0, 1) == True
    assert board.matrix.item((4,0)) == 1

    assert board.add_piece(0, 2) == True
    assert board.matrix.item((3,0)) == 2
    assert board.matrix.item((4,0)) == 1

    assert board.add_piece(0, 2) == True
    assert board.matrix.item((2,0)) == 2
    assert board.matrix.item((3,0)) == 2
    assert board.matrix.item((4,0)) == 1

    assert board.add_piece(1, 1) == True
    assert board.matrix.item((4,1)) == 1

    assert board.add_piece(4, 1) == True
    assert board.matrix.item((4,4)) == 1

"""
Tests that the board can be filled up completely 
but no more.
"""
def test_add_piece_max_column():
    board = Board(5,5)

    # Fill board
    for x in range(board.columns):
        for y in range(board.rows):
            assert board.add_piece(x, 1) == True

    # Attempt to overfill
    for x in range(board.columns):
        assert board.add_piece(x, 2) == False

    # Make sure initially filled values weren't overriden
    for x in range(board.columns):
        for y in range(board.rows):
            assert board.matrix.item((x,y)) == 1
