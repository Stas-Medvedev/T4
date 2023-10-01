from board import Board
import re
import pytest

def test_update_board() -> None:
    board = Board()
    board.update(1, 'X')
    
    assert board.available_positions == list(range(2,10))
    assert board.markers == ['X'] + [' '] * 8

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

def test_from_string_one_proper_marker() -> None:
    board_string = \
'''
 | | 
-+-+-
 |X| 
-+-+-
 | | 
'''
    board_string_2 = \
'''
 | | 
-+-+-
 | | 
-+-+-
O| | 
'''

    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == [1, 2, 3, 4, 6, 7, 8, 9]
    assert board.markers == [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
    assert board_2.available_positions == [2, 3, 4, 5, 6, 7, 8, 9]
    assert board_2.markers == ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def test_from_string_two_proper_markers() -> None:
    board_string = \
'''
 | | 
-+-+-
 |X| 
-+-+-
O| | 
'''
    board_string_2 = \
'''
X| | 
-+-+-
O| | 
-+-+-
 | | 
'''
    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == [2, 3, 4, 6, 7, 8, 9]
    assert board.markers == ['O', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
    assert board_2.available_positions == [1, 2, 3, 5, 6, 8, 9]
    assert board_2.markers == [' ', ' ', ' ', 'O', ' ', ' ', 'X', ' ', ' ']

def test_from_string_three_proper_markers() -> None:
    board_string = \
'''
 | |X
-+-+-
 |X| 
-+-+-
O| | 
'''
    board_string_2 = \
'''
 | |X
-+-+-
 | | 
-+-+-
 |X|O
'''
    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == [2, 3, 4, 6, 7, 8]
    assert board.markers == ['O', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
    assert board_2.available_positions == [1, 4, 5, 6, 7, 8]
    assert board_2.markers == [' ', 'X', 'O', ' ', ' ', ' ', ' ', ' ', 'X']

def test_from_string_four_proper_markers() -> None:
    board_string = \
'''
 | |X
-+-+-
 |X| 
-+-+-
O| |O
'''
    board_string_2 = \
'''
 | | 
-+-+-
X|O|O
-+-+-
 |X| 
'''
    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == [2, 4, 6, 7, 8]
    assert board.markers == ['O', ' ', 'O', ' ', 'X', ' ', ' ', ' ', 'X']
    assert board_2.available_positions == [1, 3, 7, 8, 9]
    assert board_2.markers == [' ', 'X', ' ', 'X', 'O', 'O', ' ', ' ', ' ']

def test_from_string_five_proper_markers() -> None:
    board_string = \
'''
 | |X
-+-+-
 |X| 
-+-+-
O|X|O
'''
    board_string_2 = \
'''
O|X| 
-+-+-
X|X| 
-+-+-
 |O| 
'''
    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == [4, 6, 7, 8]
    assert board.markers == ['O', 'X', 'O', ' ', 'X', ' ', ' ', ' ', 'X']
    assert board_2.available_positions == [1, 3, 6, 9]
    assert board_2.markers == [' ', 'O', ' ', 'X', 'X', ' ', 'O', 'X', ' ']

def test_from_string_six_proper_markers() -> None:
    board_string = \
'''
 |O|X
-+-+-
 |X| 
-+-+-
O|X|O
'''
    board_string_2 = \
'''
X|O| 
-+-+-
X|O| 
-+-+-
O|X| 
'''
    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == [4, 6, 7]
    assert board.markers == ['O', 'X', 'O', ' ', 'X', ' ', ' ', 'O', 'X']
    assert board_2.available_positions == [3, 6, 9]
    assert board_2.markers == ['O', 'X', ' ', 'X', 'O', ' ', 'X', 'O', ' ']

def test_from_string_seven_proper_markers() -> None:
    board_string = \
'''
 |O|X
-+-+-
 |X|X
-+-+-
O|X|O
'''
    board_string_2 = \
'''
X|O| 
-+-+-
O|O| 
-+-+-
O|X|X
'''
    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == [4, 7]
    assert board.markers == ['O', 'X', 'O', ' ', 'X', 'X', ' ', 'O', 'X']
    assert board_2.available_positions == [6, 9]
    assert board_2.markers == ['O', 'X', 'X', 'O', 'O', ' ', 'X', 'O', ' ']

def test_from_string_eight_proper_markers() -> None:
    board_string = \
'''
 |O|X
-+-+-
O|X|X
-+-+-
O|X|O
'''
    board_string_2 = \
'''
X|O|O
-+-+-
O|O|X
-+-+-
 |X|X
'''

    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == [7]
    assert board.markers == ['O', 'X', 'O', 'O', 'X', 'X', ' ', 'O', 'X']
    assert board_2.available_positions == [1]
    assert board_2.markers == [' ', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O']

def test_from_string_nine_proper_markers() -> None:
    board_string = \
'''
X|O|X
-+-+-
O|X|X
-+-+-
O|X|O
'''
    board_string_2 = \
'''
O|X|X
-+-+-
O|X|O
-+-+-
X|O|X
'''
    
    board = Board.from_string(board_string)
    board_2 = Board.from_string(board_string_2)

    assert board.available_positions == []
    assert board.markers == ['O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X']
    assert board_2.available_positions == []
    assert board_2.markers == ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X']

def test_from_string_invalid_format() -> None:
    board_string_1 = \
'''
 | | 
---+-
 | | 
'''
    board_string_2 = \
'''
X|O|X
'''

    with pytest.raises(ValueError, match=re.escape("Invalid board format. Must be 5 rows, including the separators.")):
        board = Board.from_string(board_string_1)
    with pytest.raises(ValueError, match=re.escape("Invalid board format. Must be 5 rows, including the separators.")):
        board = Board.from_string(board_string_2)

def test_from_string_separator_error() -> None:
    board_string = \
'''
 | | 
---+-
 | | 
-+-+-
 | | 
'''
    board_string_2 = \
'''
 | | 
-+-+-
 | | 
-_---
 | | 
'''
    with pytest.raises(ValueError, match=re.escape("Invalid board: Separator rows must be in '-+-+-' format")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Invalid board: Separator rows must be in '-+-+-' format")):
        board = Board.from_string(board_string_2)

def test_from_string_too_many_characters_in_row_error() -> None:
    board_string = \
'''
 | | 
-+-+-
 | |XX
-+-+-
 | | 
'''
    board_string_2 = \
'''
OO| | 
-+-+-
 | | 
-+-+-
 | | 
'''
    with pytest.raises(ValueError, match=re.escape("Too many characters in row 2")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Too many characters in row 1")):
        board = Board.from_string(board_string_2)

def test_from_string_not_enough_characters_in_row_error() -> None:
    board_string = \
'''
| | 
-+-+-
 | | 
-+-+-
 | | 
'''
    board_string_2 = \
'''
 | | 
-+-+-
 | | 
-+-+-
 | |
'''
    with pytest.raises(ValueError, match=re.escape("Not enough characters in row 1")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Not enough characters in row 3")):
        board = Board.from_string(board_string_2)

def test_from_string_invalid_marker() -> None:
    board_string = \
'''
 | | 
-+-+-
 | | 
-+-+-
XXX| 
'''
    board_string_2 = \
'''
 |OOO
-+-+-
 | | 
-+-+-
 | | 
'''
    with pytest.raises(ValueError, match=re.escape("Invalid marker passed: XXX")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Invalid marker passed: OOO")):
        board = Board.from_string(board_string_2)

def test_from_string_too_many_marker_types() -> None:
    board_string = \
'''
 | | 
-+-+-
 | | 
-+-+-
X|O|P
'''
    board_string_2 = \
'''
 |Q| 
-+-+-
 | | 
-+-+-
X|O| 
'''
    with pytest.raises(ValueError, match=re.escape("Invalid board: too many marker types")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Invalid board: too many marker types")):
        board = Board.from_string(board_string_2)

def test_from_string_one_marker_board() -> None:
    board_string = \
'''
X|X|X
-+-+-
X|X|X
-+-+-
X|X|X
'''
    board_string_2 = \
'''
O|O|O
-+-+-
O|O|O
-+-+-
O|O|O
'''
    with pytest.raises(ValueError, match=re.escape("Invalid board: only one marker passed with no spaces")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Invalid board: only one marker passed with no spaces")):
        board = Board.from_string(board_string_2)

def test_from_string_double_marker_board() -> None:
    board_string = \
'''
 | | 
-+-+-
 | | 
-+-+-
X| |X
'''
    board_string_2 = \
'''
O| | 
-+-+-
 | | 
-+-+-
O| | 
'''
    with pytest.raises(ValueError, match=re.escape("Invalid board: only one marker passed, and it appears more than once")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Invalid board: only one marker passed, and it appears more than once")):
        board = Board.from_string(board_string_2)

def test_from_string_incorrect_full_board() -> None:
    board_string = \
'''
O|O|O
-+-+-
O|X|O
-+-+-
X|O|X
'''
    board_string_2 = \
'''
O|X|X
-+-+-
X|X|O
-+-+-
X|O|X
'''
    with pytest.raises(ValueError, match=re.escape("Invalid board: marker counts have to be 5 and 4 for a full board")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Invalid board: marker counts have to be 5 and 4 for a full board")):
        board = Board.from_string(board_string_2)

def test_from_string_full_board_too_many_markers() -> None:
    board_string = \
'''
O|A|O
-+-+-
O|X|O
-+-+-
X|O|X
'''
    board_string_2 = \
'''
o|X|O
-+-+-
X|X|O
-+-+-
X|O|X
'''
    with pytest.raises(ValueError, match=re.escape("Invalid board: too many markers. Markers:")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Invalid board: too many markers. Markers:")):
        board = Board.from_string(board_string_2)

def test_from_string_incorrect_marker_count() -> None:
    board_string = \
'''
 | | 
-+-+-
 | |X
-+-+-
X|O|X
'''
    board_string_2 = \
'''
 | | 
-+-+-
O|X|O
-+-+-
 |O| 
'''
    with pytest.raises(ValueError, match=re.escape("Invalid board: one of the markers appears too many times")):
        board = Board.from_string(board_string)
    with pytest.raises(ValueError, match=re.escape("Invalid board: one of the markers appears too many times")):
        board = Board.from_string(board_string_2)

# TODO: Add additional string examples to tests