from player import Player, Easy_CPU_Player, Medium_CPU_Player, Hard_CPU_Player
from board import Board
from ui import UI

class GameManager:
    '''
    The purpose of the GameManager class is to manage game instances.
    This class will get user input and create instances of all of the
    necessary classes. It will also keep track of scores and restarts.
    '''
    def __init__(self):
        self.board = Board()
        self.ui = UI(self.board)

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
        selection = self.ui.get_player_selection()
        
        player1 = self.get_player_object(selection[0], 'X')
        player2 = self.get_player_object(selection[1], 'O')
            
        return [player1, player2]

    def check_restart():
        '''
        Checks if the player(s) would like to play another match.
        Returns True if yes, False if no.
        Used as the conditional for the while loop in the main logic.
        Script ends when this function returns False.
        '''
        restart = input('Play again? [Y]/N:').lower()
        while restart not in ['', 'y', 'n']:
            restart = input('Play again? [Y]/N:').lower()
        if restart == 'n':
            return False
        return True

    def run(self):
        '''
        Action order:
        ============
        - [DONE] Get player selection
        - [DONE] Instantiate player objects
        - Instantiate board object
        - Instantiate game object
        - After a game is completed, check restart
        - Update scores if necessary
        '''
        players = self.get_players()
        game = Game()