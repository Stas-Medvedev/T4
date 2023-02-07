'''
This file will contain all of the interfaces used in the program.
'''
from typing import Protocol, List

class Board(Protocol):
    available_positions: List[int]
    current_markers: List[str]

    def update(self, position: int, marker: str) -> None:
        ...

class Player(Protocol):
    def take_turn(self, board: Board) -> int:
        ...

class UI(Protocol):
    def get_player_selection() -> tuple[str, str]:
        ...

    def select_CPU_difficulty() -> str:
        ...

    def display_board(board: Board) -> None:
        ...

    def display_instructions() -> None:
        ... 