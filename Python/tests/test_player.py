from Python import player
from pytest import MonkeyPatch

def test_human_player(monkeypatch: MonkeyPatch) -> None:
    player = player.Player(name='Test', marker='X')