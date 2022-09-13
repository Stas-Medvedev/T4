# winning positions
# rows: 0,1,2; 3,4,5; 6,7,8;
# columns: 0,3,6; 1,4,7; 2,5,8;
# diagonals: 0,4,8; 2,4,6;

# TODO:
#       create Game class
#       create Player and CPU_Player classes
#       Player will hold human player info: name, marker and function to play the game: make_move
#       CPU_Player will inherit from Player and override place_marker
#       create a turn function for easy computer difficulty (random.choice)
#       create a turn algorithm for impossible difficulty
#           - check if center is available, if it is, take it
#           - create can_win function which checks all of the winning positions and looks for one that
#               has two current player's markers and an empty space
#           - create have_to_cover function which is similar to above but checks for opponent's markers
#           - create can_fork function which will look through pairs of winning positions
#               looking for a pair that has one marker and two spaces in each where a space is shared by
#               both positions
#       create a medium difficulty randomly choosing turns from easy and impossible

import Game
import Player

def select_players():
        '''
        "Player vs player" or "player vs CPU" game mode selector.
        Returns a pair of Player objects that will be used to create a Game object.
        '''
        choices = {1: ("player", "player"), 2: ("player", "cpu"), 3: ("cpu", "player")}
        print('1 - Player (X) vs Player (O)')
        print('2 - Player (X) vs CPU (O)')
        print('3 - CPU (X) vs Player(O)')
        choice = input('Select game mode ([1],2,3):')
        while choice not in ['', '1', '2', '3']:
            choice = input('Select game mode ([1],2,3):')
        if choice == '':
            selection = choices[1]
        else:
            selection = choices[int(choice)]
        
        players = []
        for i in range(2):
            if i == 0:
                marker = 'X'
            else:
                marker = 'O'
            if selection[i] == 'player':
                player_name = input(f'Please enter name for player {i+1}:')
                players.append(Player.Player(player_name, marker))
            else:
                player_name = 'CPU'
                players.append(Player.CPU_Player(player_name, marker))
            
        return players

def get_game_object(players):
    '''
    Accepts an interable with players, and returns a game object with those player types.
    '''
    return Game.Game(players[0], players[1])


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

# TODO: Write a `main()` function

if __name__ == '__main__':
    
    restart = True
    while restart:        
        restart = check_restart()