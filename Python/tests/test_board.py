from board import Board

def test_update_board() -> None:
    board = Board()
    board.update(1, 'X')
    assert board.available_positions == list(range(2,10))
    assert board.markers == ['X'] + [' ']*8