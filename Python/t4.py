# winning positions
# rows: 0,1,2; 3,4,5; 6,7,8;
# columns: 0,3,6; 1,4,7; 2,5,8;
# diagonals: 0,4,8; 2,4,6;

# TODO:
#       (DONE) During player creation, accept a CPU difficulty argument
#       create Board class that will hold the playing board information for the current game
#       create Game class
#       (DONE) create Player and CPU_Player classes for each CPU difficulty
#       Player will hold human player info: name, marker and function to play the game: make_move
#       CPU_Player will inherit from Player and override place_marker
#       (DONE) create a turn function for easy computer difficulty (random.choice)
#       create a turn algorithm for impossible difficulty
#           - check if center is available, if it is, take it
#           - create can_win function which checks all of the winning positions and looks for one that
#               has two current player's markers and an empty space
#           - create have_to_cover function which is similar to above but checks for opponent's markers
#           - create can_fork function which will look through pairs of winning positions
#               looking for a pair that has one marker and two spaces in each where a space is shared by
#               both positions
#       (DONE) create a medium difficulty randomly choosing turns from easy and impossible

import Game
import Player

def get_human_player_object(marker):
    '''
    Returns a player object for human players.
    Takes marker as an argument passed from the calling function to make sure
    that the first player get 'X' and second gets 'O'.
    This can be changed in the future, possibly allowing both players to play
    with the same marker.
    '''
    name = input('Enter player name:')

    return Player.Player(name, marker)

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

def get_cpu_player_object(marker):
    '''
    Return a CPU_Player object based on selected difficulty.
    '''
    difficulty = select_CPU_difficulty()
    if difficulty == 'easy':
        return Player.Easy_CPU_Player('CPU', marker)
    elif difficulty == 'medium':
        return Player.Medium_CPU_Player('CPU', marker)
    else:
        return Player.Hard_CPU_Player('CPU', marker)

def get_player_object(kind, marker):
    if kind == 'human':
        player = get_human_player_object(marker)
    else:
        player = get_cpu_player_object(marker)

    return player

def get_player_selection():
    '''
    Prompts the user to make a player type selection, and returns a tuple of player types
    that is used to generate the appropriate player objects.
    '''
    player_pairs = {1: ("player", "player"), 2: ("player", "cpu"), 3: ("cpu", "player")}
    print('1 - Player (X) vs Player (O)')
    print('2 - Player (X) vs CPU (O)')
    print('3 - CPU (X) vs Player(O)')
    choice = input('Select game mode ([1],2,3):')
    while choice not in ['', '1', '2', '3']:
        choice = input('Select game mode ([1],2,3):')
    if choice == '':
        choice = '1'

    return player_pairs[choice]
    
def get_players():
    '''
    "Player vs player" or "player vs CPU" game mode selector.
    Returns a pair of Player objects that will be used to create a Game object.
    '''
    selection = get_player_selection()
    
    player1 = get_player_object(selection[0], 'X')
    player2 = get_player_object(selection[1], 'O')
        
    return [player1, player2]

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