# TODO:
#       work on separating and encorporating the responsibilities of the UI and Game classes
#           - which one exactly does what?
#           - if UI is responsible for displaying and intake all of the information,
#             how do I integrate the Game class methods into it?
#           - do I call the UI methods from within the Game class to run the game?
#           - Game should probably create an instance of the UI class rather than the other way around
#           - that means modifying the current setup of the UI initializer
#           - that also means that Game class won't get player in the __init__ but at some point later
#       Add type hints to functions
#       Remove board as an object attribute in the player class and instead pass the current board 
#           from the game class when calling the take_turn method
#       Look into abstracting the Player and UI classes in the Game class by using protocols
#           - add necessary methods for the UI class to the protocol
#           - consider using a protocol for Board as well
#       Consider building the restart check and scorekeeping functionality into the Game class
#           This won't allow usage of Protocol for the Board class. Consider building a GameLauncher
#           class or something along those lines that will create Game class instances. Or just
#           avoid using Protocol for Board within the Game class
#       UI class has display_board and display_current_board methods. Is the second one needed?
#       Start running the code to debug

def check_restart() -> bool:
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