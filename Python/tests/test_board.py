from board import Board
import pytest

def test_update_board() -> None:
    board = Board()
    board.update(1, 'X')
    
    assert board.available_positions == list(range(2,10))
    assert board.markers == ['X'] + [' '] * 8

# TODO: Write several test for various possible from_string inputs
# Can use some from test cases for player

def test_from_string_blank() -> None:
    board_string = \
'''
 | | 
-+-+-
 | | 
-+-+-
 | | 
'''
    board = Board.from_string(board_string)
    
    assert board.available_positions == list(range(1,10))
    assert board.markers == [' '] * 9