from board import Board

# add protocols for Player and UI classes
# add UI object implementation
# add type hints

class Game:
    winning_positions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__(self, player1, player2):
        # pass two player objects upon initialization
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.board = Board()

    def change_current_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def accept_turn(self):
        '''
        Takes in a position, makes sure the position is available,
        calls update_grid to update current_positions and available_positions,
        and displays the updated game grid.
        '''
        position = self.current_player.take_turn(self)
        while position not in self.available_positions:
            position = self.current_player.take_turn(self)
        self.update_grid(position, self.current_player.marker)
        self.display_grid(self.current_positions)

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