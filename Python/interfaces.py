'''
This file will contain all of the interfaces used in the program.
'''
from typing import Protocol, List

class Board(Protocol):
    available_positions: List[int]
    current_markers: List[str]