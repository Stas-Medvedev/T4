import player
import game

class UI:
    def __init__(self):
        players = self.get_players()
        return self.get_game_object(players)
    
    def select_CPU_difficulty():
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

    def get_cpu_player_object(self, marker):
        '''
        Return a CPU_Player object based on selected difficulty.
        '''
        difficulty = self.select_CPU_difficulty()
        if difficulty == 'easy':
            return player.Easy_CPU_Player('CPU', marker)
        elif difficulty == 'medium':
            return player.Medium_CPU_Player('CPU', marker)
        else:
            return player.Hard_CPU_Player('CPU', marker)

    def get_human_player_object(marker):
        '''
        Returns a player object for human players.
        Takes marker as an argument passed from the calling function to make sure
        that the first player get 'X' and second gets 'O'.
        This can be changed in the future, possibly allowing both players to play
        with the same marker.
        '''
        name = input('Enter player name:')

        return player.Player(name, marker)

    def get_player_object(self, player_type, marker):
        if player_type == 'human':
            player = self.get_human_player_object(marker)
        else:
            player = self.get_cpu_player_object(marker)

        return player

    def get_player_selection():
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
        
    def get_players(self):
        '''
        "Player vs player" or "player vs CPU" game mode selector.
        Returns a pair of Player objects that will be used to create a Game object.
        '''
        selection = self.get_player_selection()
        
        player1 = self.get_player_object(selection[0], 'X')
        player2 = self.get_player_object(selection[1], 'O')
            
        return [player1, player2]

    def get_game_object(players):
        '''
        Accepts an interable with players, and returns a game object with those player types.
        '''
        return game.Game(players[0], players[1])