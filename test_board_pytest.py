from board import Board

def test_addPiece():
    board = Board(5,5)
    board.addPiece(0, 1)
    assert board.boardMatrix.item((4,0)) == 1
