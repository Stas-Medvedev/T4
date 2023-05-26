import player
from board import Board
from pytest import MonkeyPatch

# TODO: Make a function that will convert a string representation of a board
# like shown below into arrays that can be set as Board object attributes

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

def test_Easy_cpu() -> None:
    test_player = player.Easy_CPU_Player(name='CPU', marker='X')
    board = Board()
    position = test_player.take_turn(board)
    assert position in board.available_positions