import player
from board import Board
from pytest import MonkeyPatch

# TODO: Write tests for Hard_CPU
# TODO: Add additional test cases for existing tests
#   - Decide if need to write new tests or can add another assert for human player
#   - Learn how to supply multiple human inputs in PyTest (parametrize?)
#       -- Need multiple inputs within the same call
#       -- https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9
# TODO: Plan future work
# TODO: Start converting text boards into board objects
#       - Convert comments below into board strings

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

board_string_1b = \
'''
X| | 
-+-+-
 | | 
-+-+-
 | | 
'''

board_1a = Board.from_string(board_string_1a)
board_1b = Board.from_string(board_string_1b)

board_string_2a = \
'''
 | |X
-+-+-
O|X| 
-+-+-
 |O| 
'''

board_string_2b = \
'''
X|X| 
-+-+-
 |X| 
-+-+-
O| |O
'''

board_string_2c = \
'''
X| |X
-+-+-
O|X| 
-+-+-
O|O| 
'''

board_string_2d = \
'''
X|O| 
-+-+-
X|X|O
-+-+-
 |X|O
'''

board_2a = Board.from_string(board_string_2a)
board_2b = Board.from_string(board_string_2b)
board_2c = Board.from_string(board_string_2c)
board_2d = Board.from_string(board_string_2d)

board_string_3a = \
'''
 | |O
-+-+-
X|O| 
-+-+-
 |X| 
'''

board_string_3b = \
'''
O|X| 
-+-+-
X|X| 
-+-+-
 |O| 
'''

board_3a = Board.from_string(board_string_3a)
board_3b = Board.from_string(board_string_3b)

# TODO: Add boards for check_diagonal_case