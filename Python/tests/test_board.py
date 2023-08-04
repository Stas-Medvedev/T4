from board import Board
import re
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

def test_from_string_nine_proper_markers() -> None:
    board_string = \
'''
X|O|X
-+-+-
O|X|X
-+-+-
O|X|O
'''
    board = Board.from_string(board_string)

    assert board.available_positions == []
    assert board.markers == ['O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X']

# TODO: Add tests for errors
# TODO: Look into pytest.raises

def test_from_string_separator_error() -> None:
    board_string = \
'''
 | | 
---+-
 | | 
-+-+-
 | | 
'''
    with pytest.raises(ValueError, match=re.escape("Invalid board: Separator rows must be in '-+-+-' format")):
        board = Board.from_string(board_string)

def test_from_string_too_many_characters_in_row_error() -> None:
    board_string = \
'''
 | | 
-+-+-
 | |XX
-+-+-
 | | 
'''
    with pytest.raises(ValueError, match=re.escape("Too many characters in row 2")):
        board = Board.from_string(board_string)