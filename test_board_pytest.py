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

"""
Tests that get_ai_move fills the board completely with 
random moves.
"""
def test_get_ai_move():
    board = Board(7,7)

    # Fill board with ai moves.
    for x in range(board.columns):
        for y in range(board.rows):
            ai_move = board.get_ai_move()
            assert board.add_piece(ai_move, 1) == True

    # Test that board is filled.
    for x in range(board.columns):
        for y in range(board.rows):
            assert board.matrix.item((y, x)) == 1

"""
Tests that get_ai_move returns -1 when there are no
more moves available.
"""
def test_ai_out_of_moves():
    board = Board(7,7)
    
    # Fill board with ai moves.
    for x in range(board.columns):
        for y in range(board.rows):
            ai_move = board.get_ai_move()
            assert board.add_piece(ai_move, 1) == True

    # Perform test.
    for i in range(20):
        assert board.get_ai_move() == -1

"""
Tests initial board evaluation.
"""
def test_evaluate_board_initial():
    board = Board(7,7)
    assert board.evaluate_board() == 0

"""
Tests horizontal board evaluation.
"""
def test_evaluate_board_horizontal():
    board = Board(7,7)

    for x in range(0,4):
        board.add_piece(x,1)

    assert board.evaluate_board() == 1

    board = Board(7,7)

    for x in range(0,3):
        board.add_piece(x,1)
        board.add_piece(x+1,2)

    assert board.evaluate_board() == 0
