from ui import UI
from pytest import MonkeyPatch

def test_get_player_selection_1(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['4', '/', 'b', '1'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.get_player_selection()
    assert choice == ("human", "human")

def test_get_player_selection_2(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['a', '8', '2'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.get_player_selection()
    assert choice == ("human", "cpu")

def test_get_player_selection_3(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['X', '3'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.get_player_selection()
    assert choice == ("cpu", "human")

def test_get_player_selection_4(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['Y', ''])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.get_player_selection()
    assert choice == ("human", "human")

def test_select_CPU_difficulty_1(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['4', '/', 'b', '1'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.select_CPU_difficulty()
    assert choice == 'easy'

def test_select_CPU_difficulty_2(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['a', '8', '2'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.select_CPU_difficulty()
    assert choice == 'medium'

def test_select_CPU_difficulty_3(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['X', '3'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.select_CPU_difficulty()
    assert choice == 'hard'

def test_select_CPU_difficulty_4(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['Y', ''])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.select_CPU_difficulty()
    assert choice == 'easy'

def test_check_restart_yes(monkeypatch: MonkeyPatch) -> None:
    inputs = iter(['a', '8', 'Y'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    choice = UI.check_restart()
    assert choice == True