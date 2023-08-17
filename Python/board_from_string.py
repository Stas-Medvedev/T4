# File to check performance of the from_string method of the Board class
from board import Board

board_string = \
'''
 | | 
-+-+-
 | | 
-+-+-
XXX| 
'''

board = Board.from_string(board_string)     # raises "ValueError: Invalid marker passed: XXX"

print(f"Markers: {board.markers}")
print(f"Available positions: {board.available_positions}")