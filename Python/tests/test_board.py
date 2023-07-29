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

def test_from_string_single_marker() -> None:
    board_string = \
'''
 | | 
-+-+-
 |X| 
-+-+-
 | | 
'''
    board = Board.from_string(board_string)

    assert board.available_positions == [1, 2, 3, 4, 6, 7, 8, 9]
    assert board.markers == [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']

def test_from_string_two_single_markers() -> None:
    board_string = \
'''
 | | 
-+-+-
 |X| 
-+-+-
O| | 
'''
    board = Board.from_string(board_string)

    assert board.available_positions == [2, 3, 4, 6, 7, 8, 9]
    assert board.markers == ['O', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']

def test_from_string_three_proper_markers() -> None:
    board_string = \
'''
 | |X
-+-+-
 |X| 
-+-+-
O| | 
'''
    board = Board.from_string(board_string)

    assert board.available_positions == [2, 3, 4, 6, 7, 8]
    assert board.markers == ['O', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']

def test_from_string_four_proper_markers() -> None:
    board_string = \
'''
 | |X
-+-+-
 |X| 
-+-+-
O| |O
'''
    board = Board.from_string(board_string)

    assert board.available_positions == [2, 4, 6, 7, 8]
    assert board.markers == ['O', ' ', 'O', ' ', 'X', ' ', ' ', ' ', 'X']

def test_from_string_five_proper_markers() -> None:
    board_string = \
'''
 | |X
-+-+-
 |X| 
-+-+-
O|X|O
'''
    board = Board.from_string(board_string)

    assert board.available_positions == [4, 6, 7, 8]
    assert board.markers == ['O', 'X', 'O', ' ', 'X', ' ', ' ', ' ', 'X']

def test_from_string_six_proper_markers() -> None:
    board_string = \
'''
 |O|X
-+-+-
 |X| 
-+-+-
O|X|O
'''
    board = Board.from_string(board_string)

    assert board.available_positions == [4, 6, 7]
    assert board.markers == ['O', 'X', 'O', ' ', 'X', ' ', ' ', 'O', 'X']

def test_from_string_seven_proper_markers() -> None:
    board_string = \
'''
 |O|X
-+-+-
 |X|X
-+-+-
O|X|O
'''
    board = Board.from_string(board_string)

    assert board.available_positions == [4, 7]
    assert board.markers == ['O', 'X', 'O', ' ', 'X', 'X', ' ', 'O', 'X']

def test_from_string_eight_proper_markers() -> None:
    board_string = \
'''
 |O|X
-+-+-
O|X|X
-+-+-
O|X|O
'''
    board = Board.from_string(board_string)

    assert board.available_positions == [7]
    assert board.markers == ['O', 'X', 'O', 'O', 'X', 'X', ' ', 'O', 'X']