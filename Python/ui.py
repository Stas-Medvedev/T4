from player import Player, Easy_CPU_Player, Medium_CPU_Player, Hard_CPU_Player
from game import Game
from board import Board

'''
TODO:
    - Go through the functions and see if any of them need to be moved to the GameManager class
    - Check if any of the imports can be replaced with interfaces
'''

class UI:
    def __init__(self, board: Board):
        self.board = board
    
    def get_player_selection() -> tuple[str, str]:
        '''
        Prompts the user to make a player type selection, and returns a tuple of player types
        that is used to generate the appropriate player objects.
        '''
        player_pairs = {'1': ("player", "player"), '2': ("player", "cpu"), '3': ("cpu", "player")}
        print('1 - Player (X) vs Player (O)')
        print('2 - Player (X) vs CPU (O)')
        print('3 - CPU (X) vs Player (O)')
        choice = input('Select game mode ([1],2,3):')
        while choice not in ['', '1', '2', '3']:
            choice = input('Select game mode ([1],2,3):')
        if choice == '':
            choice = '1'

        return player_pairs[choice]
        
    def select_CPU_difficulty() -> str:
        '''
        Lets the user select CPU difficulty and returns a string that is used by
        get_cpu_player_object() to return the appropriate CPU_Player object.
        '''
        difficulties = {'1':'easy', '2':'medium', '3':'hard'}
        choice = input('Select CPU difficulty: [1] - Easy, 2 - Medium, 3 - Hard:')
        while choice not in ['', '1', '2', '3']:
                choice = input('Select CPU difficulty: [1] - Easy, 2 - Medium, 3 - Hard:')
        if choice == '':
            choice = '1'
        
        return difficulties[choice]

    def get_cpu_player_object(self, marker: str) -> Player:
        '''
        Return a CPU_Player object based on selected difficulty.
        '''
        difficulty = self.select_CPU_difficulty()
        if difficulty == 'easy':
            return Easy_CPU_Player('CPU', marker)
        elif difficulty == 'medium':
            return Medium_CPU_Player('CPU', marker)
        else:
            return Hard_CPU_Player('CPU', marker)

    def get_human_player_object(marker: str) -> Player:
        '''
        Returns a player object for human players.
        Takes marker as an argument passed from the calling function to make sure
        that the first player gets 'X' and second gets 'O'.
        This can be changed in the future, possibly allowing both players to play
        with the same marker.
        '''
        name = input('Enter player name:')

        return Player(name, marker)

    def get_player_object(self, player_type: str, marker: str) -> Player:
        if player_type == 'human':
            player = self.get_human_player_object(marker)
        else:
            player = self.get_cpu_player_object(marker)

        return player

    def get_players(self) -> list[Player]:
        '''
        "Player vs player" or "player vs CPU" game mode selector.
        Returns a pair of Player objects that will be used to create a Game object.
        '''
        selection = self.get_player_selection()
        
        player1 = self.get_player_object(selection[0], 'X')
        player2 = self.get_player_object(selection[1], 'O')
            
        return [player1, player2]

    def display_board(self, markers: list[str]) -> None:
        '''
        Displays the playing board with the provided markers.
        '''
        row1 = "|".join(x for x in markers[:3])
        row2 = "|".join(x for x in markers[3:6])
        row3 = "|".join(x for x in markers[6:])
        row_separator = '-+-+-'
        print()
        print(row3)
        print(row_separator)
        print(row2)
        print(row_separator)
        print(row1)
        print()

    def display_instructions(self) -> None:
        '''
        Displays instructions and the cell numbers.
        '''
        print('Classic tic-tac-toe. To play, select a position number to place your marker according to the grid below')
        self.display_board([str(x) for x in range(1, 10)])

    def display_current_board(self) -> None:
        '''
        Displays the current playing board.
        '''
        self.display_board(self.board.current_markers)