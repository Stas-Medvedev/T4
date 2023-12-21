import player
from board import Board
from pytest import MonkeyPatch

# TODO: Add tests for individual move functions each test using all of the boards
        # - Move board creation outside individual tests
        # - Create reusable test player objects outside the tests
        # - Redo the tests to test specific move functions instead of their performance as part of take_turn

# TODO: Write tests for Hard_CPU
# TODO: Add additional test cases for existing tests
#   - Decide if need to write new tests or can add another assert for human player
#   - Learn how to supply multiple human inputs in PyTest (parametrize?)
#       -- Need multiple inputs within the same call
#       -- https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9

# Look into parameterizing tests for CPU players with different boards
# Create multiple boards for different games scenarios
# and test each CPU class on those boards (mostly, this is for Hard CPU)
# docs for reference: https://docs.pytest.org/en/6.2.x/parametrize.html

# The boards below are intended to be used as tests for Hard_CPU_Player.take_turn()
# They can also be used as test for individual turn sub-functions
# as long as expected returns are adjusted accordingly.

# Generating boards for testing:
# Need at least one board to test each of the Hard_CPU move sub-routines
# 
# Sub-routines and boards
# =======================
# 
# Take 5 if available:
# As X       As O
#  | |       X| |
# -+-+-      -+-+-
#  | |        | |
# -+-+-      -+-+-
#  | |        | | 
#
# Can win:
# As X       As O
#  | |X      X|X|
# -+-+-      -+-+-
# O|x|        |X|
# -+-+-      -+-+-
#  |O|       O| |O
# 
# As X       As O
# X| |X      X|O|
# -+-+-      -+-+-
# O|x|       X|X|O
# -+-+-      -+-+-
# O|O|        |X|O
#
# Need to cover:
# As X       As O
#  | |O      O|X|
# -+-+-      -+-+-
# X|O|       X|X|
# -+-+-      -+-+-
#  |X|        |O|
#
# Check diagonal case:
# As O       As O
# X| |        | |X
# -+-+-      -+-+-
#  |O|        |O|
# -+-+-      -+-+-
#  | |X      X| |
#
# Can fork:
# As X       As O
# X| |        |X|
# -+-+-      -+-+-
# O|X|       X|O|X
# -+-+-      -+-+-
#  | |O       |O|
# 
# Take corner or side:
# As X       As O
#  |O|X       | |X
# -+-+-      -+-+-
#  |X|O      X|X|O
# -+-+-      -+-+-
# O|X|O      O| |
# 
# As X       As O
#  | |        | |
# -+-+-      -+-+-
#  |X|        |X|
# -+-+-      -+-+-
# O| |        | |
# 
# Convert tha above boards into arrays for Board objects
# Using the Board.from_string method

def test_human_player(monkeypatch: MonkeyPatch) -> None:
    test_player = player.Player(name='Test', marker='X')
    board = Board()
    monkeypatch.setattr("builtins.input", lambda _: "5")
    position = test_player.take_turn(board)
    assert position == 5

def test_human_player_multiple_inputs(monkeypatch: MonkeyPatch) -> None:
    test_player = player.Player(name='Test', marker='X')
    board = Board()
    inputs = iter(['X', '3'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    position = test_player.take_turn(board)
    assert position == 3

def test_human_player_multiple_inputs_2(monkeypatch: MonkeyPatch) -> None:
    test_player = player.Player(name='Test', marker='X')
    board = Board()
    inputs = iter(['X', 'a', '4'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    position = test_player.take_turn(board)
    assert position == 4


def test_human_player_multiple_inputs_3(monkeypatch: MonkeyPatch) -> None:
    test_player = player.Player(name='Test', marker='X')
    board = Board()
    board.available_positions = [3, 4, 5, 6, 7, 8, 9]
    inputs = iter(['1', '2', '3'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    position = test_player.take_turn(board)
    assert position == 3

def test_Easy_cpu() -> None:
    test_player = player.Easy_CPU_Player(name='CPU', marker='X')
    board = Board()
    position = test_player.take_turn(board)
    assert position in board.available_positions

board_string_1a = \
'''
 | | 
-+-+-
 | | 
-+-+-
 | | 
'''
board_1a_x = Board.from_string(board_string_1a)

board_string_2a = \
'''
 | |X
-+-+-
O|X| 
-+-+-
 |O| 
'''
board_2a_x = Board.from_string(board_string_2a)

board_string_2c = \
'''
X| |X
-+-+-
O|X| 
-+-+-
O|O| 
'''
board_2c_x = Board.from_string(board_string_2c)

board_string_3a = \
'''
 | |O
-+-+-
X|O| 
-+-+-
 |X| 
'''
board_3a_x = Board.from_string(board_string_3a)

board_string_5a = \
'''
X| | 
-+-+-
O|X| 
-+-+-
 | |O
'''
board_5a_x = Board.from_string(board_string_5a)

board_string_6a = \
'''
 |O|X
-+-+-
 |X|O
-+-+-
O|X|O
'''
board_6a_x = Board.from_string(board_string_6a)

board_string_6c = \
'''
 | | 
-+-+-
 |X| 
-+-+-
O| | 
'''
board_6c_x = Board.from_string(board_string_6c)

board_string_1b = \
'''
X| | 
-+-+-
 | | 
-+-+-
 | | 
'''
board_1b_o = Board.from_string(board_string_1b)

board_string_2b = \
'''
X|X| 
-+-+-
 |X| 
-+-+-
O| |O
'''
board_2b_o = Board.from_string(board_string_2b)

board_string_2d = \
'''
X|O| 
-+-+-
X|X|O
-+-+-
 |X|O
'''
board_2d_o = Board.from_string(board_string_2d)

board_string_3b = \
'''
O|X| 
-+-+-
X|X| 
-+-+-
 |O| 
'''
board_3b_o = Board.from_string(board_string_3b)

board_string_4a = \
'''
X| | 
-+-+-
 |O| 
-+-+-
 | |X
'''
board_4a_o = Board.from_string(board_string_4a)

board_string_4b = \
'''
 | |X
-+-+-
 |O| 
-+-+-
X| | 
'''
board_4b_o = Board.from_string(board_string_4b)

board_string_5b = \
'''
 |X| 
-+-+-
X|O|X
-+-+-
 |O| 
'''
board_5b_o = Board.from_string(board_string_5b)

board_string_6b = \
'''
 | |X
-+-+-
X|X|O
-+-+-
O| | 
'''
board_6b_o = Board.from_string(board_string_6b)

board_string_6d = \
'''
 | | 
-+-+-
 |X| 
-+-+-
 | | 
'''
board_6d_o = Board.from_string(board_string_6d)

game_boards_X = [board_1a_x, board_2a_x, board_2c_x, board_3a_x, board_5a_x, board_6a_x, board_6c_x]
game_boards_O = [board_1b_o, board_2b_o, board_2d_o, board_3b_o, board_4a_o, board_4b_o, board_5b_o, board_6b_o, board_6d_o]

player_hard_X = player.Hard_CPU_Player(name='CPU', marker='X')
player_hard_O = player.Hard_CPU_Player(name='CPU', marker='O')

def test_can_win():
    positions_X = [player_hard_X.can_win(game_board) for game_board in game_boards_X]
    positions_O = [player_hard_O.can_win(game_board) for game_board in game_boards_O]

    assert positions_X == [0, 1, 8, 0, 0, 0, 0]
    assert positions_O == [0, 2, 9, 0, 0, 0, 0, 0, 0]

def test_need_to_cover():
    # TODO: Update need_to_cover in player.py
    positions_X = [player_hard_X.need_to_cover(game_board) for game_board in game_boards_X]
    positions_O = [player_hard_O.need_to_cover(game_board) for game_board in game_boards_O]

    assert positions_X == [0, 0, 3, 1, 0, 0, 0]
    assert positions_O == [0, 2, 1, 6, 0, 0, 0, 0, 0]

def test_check_marker():

    assert player_hard_X.check_marker('X') == True
    assert player_hard_X.check_marker(' ') == False
    assert player_hard_X.check_marker('O') == False
    assert player_hard_X.check_marker('X', own=False) == False
    assert player_hard_O.check_marker('O') == True
    assert player_hard_O.check_marker(' ', own=False) == False
    assert player_hard_O.check_marker('X') == False

def test_take_turn_take_center():

    position_1 = player_hard_X.take_turn(board_1a_x)
    position_2 = player_hard_O.take_turn(board_1b_o)

    assert position_1 == 5
    assert position_2 == 5

def test_take_turn_can_win():

    position_1 = player_hard_X.take_turn(board_2a_x)
    position_2 = player_hard_O.take_turn(board_2b_o)
    position_3 = player_hard_X.take_turn(board_2c_x)
    position_4 = player_hard_O.take_turn(board_2d_o)

    assert position_1 == 1
    assert position_2 == 2
    assert position_3 in [3, 8]
    assert position_4 == 9

def test_take_turn_need_to_cover():

    position_1 = player_hard_X.take_turn(board_3a_x)
    position_2 = player_hard_O.take_turn(board_3b_o)

    assert position_1 == 1
    assert position_2 == 6

def test_take_turn_check_diagonal_case():

    position_1 = player_hard_O.take_turn(board_4a_o)
    position_2 = player_hard_O.take_turn(board_4b_o)

    assert position_1 not in [1, 9]
    assert position_2 not in [3, 7]