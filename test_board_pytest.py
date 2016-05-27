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

def test_addPiece():
    board = Board(5,5)
    board.addPiece(0, 1)
    assert board.boardMatrix.item((4,0)) == 1
