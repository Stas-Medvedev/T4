from typing import Protocol, List
from interfaces import Board, Player

# go through the current methods and add/remove functionality as necessary
#   update methods to include changed Player.take_turn() functionality
#   take into account functionality that will be handled by GameManager
# add protocols for Player and UI classes
# add the UI class methods needed for the protocol
# add UI object implementation
#   player selection functions of UI should be in GameManager and not here
#   game class should receive all the necessary objects to run a single game
# add Board class protocol
# add type hints

class UI(Protocol):
    @staticmethod
    def get_player_selection() -> tuple[str, str]:
        ...
    
    @staticmethod
    def select_cpu_difficulty() -> str:
        ...

class Game:
    winning_positions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__(self, player1: Player, player2: Player, board: Board, ui: UI):
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.board = board
        self.ui = ui

    def change_current_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def accept_turn(self):
        '''
        Takes in a position, makes sure the position is available,
        calls update_grid to update current_positions and available_positions,
        and displays the updated game grid.
        '''
        position = self.current_player.take_turn(self)
        # The take_turn method should already be checking if the position is 
        # available. This is just to make sure. 
        while position not in self.board.available_positions:
            print(f'{position} is not an available position.')
            position = self.current_player.take_turn(self)

        '''
        update_grid and display_grid methods have been removed. There are
        replacement methods in the UI (for display_grid) and Board (for 
        update_grid) classes.
        '''

        self.board.update(position, self.current_player.marker)
        # self.display_grid(self.current_positions)
        

    def check_winner(self):
        '''
        Checks if there is a winner.
        Returns the winning position and True if there is, None and False otherwise.
        '''
        # if there have been less than 5 turns, there can't be a winner
        if len(self.available_positions) > 4:
            winning_position = None
            winner = False
            return winning_position, winner

        for positions in self.winning_positions:
            if ''.join([self.current_positions[i] for i in positions]) == self.current_player.marker * 3:
                winning_position = positions
                winner = True
                return winning_position, winner

        winning_position = None
        winner = False
        return winning_position, winner

    def display_winner(self, player, winning_position):
        '''
        Displays the board with the winning line and marker.
        Used at the end of a match with a winner.
        '''
        final_markers = [' '] * 9
        for i in winning_position:
            final_markers[i] = player.marker
        self.display_grid(final_markers)
        print(f'{player.name} won the game!')