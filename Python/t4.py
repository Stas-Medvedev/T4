# winning positions
# rows: 0,1,2; 3,4,5; 6,7,8;
# columns: 0,3,6; 1,4,7; 2,5,8;
# diagonals: 0,4,8; 2,4,6;

# TODO:
#       Maybe turn Board into a dataclass
#       work on separating and encorporating the responsibilities of the UI and Game classes
#           - which one exactly does what?
#           - if UI is responsible for displaying and intake all of the information,
#             how do I integrate the Game class methods into it?
#           - do I call the UI methods from within the Game class to run the game?
#           - Game should probably create an instance of the UI class rather than the other way around
#           - that means modifying the current setup of the UI initializer
#           - that also means that Game class won't get player in the __init__ but at some point later
#       create Game class
#       create a turn algorithm for impossible difficulty
#           - check if center is available, if it is, take it
#           - create can_win function which checks all of the winning positions and looks for one that
#               has two current player's markers and an empty space
#           - create have_to_cover function which is similar to above but checks for opponent's markers
#           - create can_fork function which will look through pairs of winning positions
#               looking for a pair that has one marker and two spaces in each where a space is shared by
#               both positions
#       Make sure all take_turn functions return a number between 1 and 9 (same as the initial available positions)

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