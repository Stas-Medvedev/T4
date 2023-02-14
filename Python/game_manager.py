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

    # Move to GameManager
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

    # Move to GameManager and replace with get_plaayer_name()
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

    # Move to GameManager
    def get_player_object(self, player_type: str, marker: str) -> Player:
        if player_type == 'human':
            player = self.get_human_player_object(marker)
        else:
            player = self.get_cpu_player_object(marker)

        return player

    # Move to GameManager
    def get_players(self) -> list[Player]:
        '''
        "Player vs player" or "player vs CPU" game mode selector.
        Returns a pair of Player objects that will be used to create a Game object.
        '''
        selection = self.get_player_selection()
        
        player1 = self.get_player_object(selection[0], 'X')
        player2 = self.get_player_object(selection[1], 'O')
            
        return [player1, player2]

    def check_restart():
        pass

    def run(self):
        pass