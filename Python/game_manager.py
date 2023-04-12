from game import Game
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
        self.ui = UI()

    def get_cpu_player_object(self, marker: str) -> Player:
        '''
        Return a CPU_Player object based on selected difficulty.
        '''
        difficulty = self.ui.select_CPU_difficulty()
        if difficulty == 'easy':
            return Easy_CPU_Player('CPU', marker)
        elif difficulty == 'medium':
            return Medium_CPU_Player('CPU', marker)
        else:
            return Hard_CPU_Player('CPU', marker)

    @staticmethod
    def get_human_player_object(marker: str, order: int) -> Player:
        '''
        Returns a player object for human players.
        Takes marker as an argument passed from the calling function to make sure
        that the first player gets 'X' and second gets 'O'.
        This can be changed in the future, possibly allowing both players to play
        with the same marker.
        '''
        name = input(f'Enter player name (player {order}): ')

        return Player(name, marker)

    def get_player_object(self, player_type: str, marker: str, order: int) -> Player:
        if player_type == 'human':
            player = self.get_human_player_object(marker, order)
        else:
            player = self.get_cpu_player_object(marker)

        return player

    def get_players(self) -> list[Player]:
        '''
        "Player vs player" or "player vs CPU" game mode selector.
        Returns a pair of Player objects that will be used to create a Game object.
        '''
        selection = self.ui.get_player_selection()
        
        player1 = self.get_player_object(selection[0], 'X', 1)
        player2 = self.get_player_object(selection[1], 'O', 2)
            
        return [player1, player2]

    def run(self) -> None:
        '''
        Action order:
        ============
        - Display instructions
        - [DONE] Get player selection
        - [DONE] Instantiate player objects
        - [DONE] Instantiate board object
        - [DONE] Instantiate game object
        - [DONE] After a game is completed, check restart
        - Update scores if necessary
        '''
        self.ui.display_instructions()
        players = self.get_players()
        player_names = [players[0].name, players[1].name]
        scores = [0, 0, 0]
        restart = True
        while restart:
            board = Board()
            game = Game(players[0], players[1], board, self.ui)
            winner = game.play()
            scores[winner] += 1
            self.ui.display_scores(player_names, scores)
            restart = self.ui.check_restart()