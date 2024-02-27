from ui import UI
from pytest import MonkeyPatch

# TODO: Write tests for other player selection choices

def test_get_plyer_selection_3(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['X', '3'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.get_player_selection()
    assert choice == ("cpu", "human")