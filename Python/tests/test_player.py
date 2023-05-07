import player
from board import Board
from pytest import MonkeyPatch

# Look into parameterizing tests for CPU players with different boards
# Create multiple boards for different games scenarios
# and test each CPU class on those boards (mostly, this is for Hard CPU)

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