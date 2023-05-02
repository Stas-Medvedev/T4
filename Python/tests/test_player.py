import player
from board import Board
from pytest import MonkeyPatch

def test_human_player(monkeypatch: MonkeyPatch) -> None:
    test_player = player.Player(name='Test', marker='X')
    board = Board()
    monkeypatch.setattr("builtins.input", "5")
    position = test_player.take_turn(board)
    assert position == 5