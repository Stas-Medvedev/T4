from interfaces import Board, Player, UI
# TODO: Look into writing unit tests for this class
class Game:
    '''
    Game class that manages an instance of one game and its dependencies.
    '''
    winning_positions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__(self, player1: Player, player2: Player, board: Board, ui: UI) -> None:
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.board = board
        self.ui = ui

    def change_current_player(self) -> None:
        '''
        Swaps the current player.
        '''
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def accept_turn(self) -> None:
        '''
        Takes in a position, makes sure the position is available,
        and updates the board with the selection.
        '''
        position = self.current_player.take_turn(self.board)
        # The take_turn method for human player checks if the position is 
        # available. This ensures that a CPU move is valid too. 
        while position not in self.board.available_positions:
            print(f'{position} is not an available position.')
            position = self.current_player.take_turn(self.board)

        self.board.update(position, self.current_player.marker)
        

    def check_winner(self) -> list | None:
        '''
        Checks if there is a winner.
        Returns the winning position if there is, None otherwise.
        '''
        # if there have been less than 5 turns, there can't be a winner
        if len(self.board.available_positions) > 4:
            return None 

        for positions in self.winning_positions:
            if ''.join([self.board.markers[i] for i in positions]) == self.current_player.marker * 3:
                return positions 

        return None 

    def display_winner(self, player, winning_position) -> None:
        '''
        Displays the board with the winning line and marker.
        Used at the end of a match with a winner.
        '''
        final_markers = [' '] * 9
        for i in winning_position:
            final_markers[i] = player.marker
        self.ui.display_board(final_markers)
        print(f'{player.name} won the game!')

    def play(self) -> int:
        '''
        Plays a game of tic-tac-toe.
        Action order:
        ============
        Take turn
        Display board
        Check winner
        If winner: display winner and end game
        Change player
        Repeat
        If there are no available positions on the board and no winner, declare a tie
        '''
        while True:
            self.accept_turn()
            self.ui.display_board(self.board.markers)
            
            winning_position = self.check_winner()
            
            if winning_position:
                self.display_winner(self.current_player, winning_position)
                if self.current_player == self.player1:
                    return 0
                return 1
            
            if self.board.available_positions == []:
                print("\nIt's a tie.\n")
                return 2
            
            self.change_current_player()