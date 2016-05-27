from board import Board

def test_addPiece():
    print("Testing adding a piece.")
    
    board = Board(5,5)
    board.addPiece(0, 1)
    assert board.boardMatrix.item(0,4) == 1
