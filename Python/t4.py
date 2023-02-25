# TODO:
#       work on separating and encorporating the responsibilities of the UI and Game classes
#           - which one exactly does what?
#           - if UI is responsible for displaying and intake all of the information,
#             how do I integrate the Game class methods into it?
#           - do I call the UI methods from within the Game class to run the game?
#           - Game should probably create an instance of the UI class rather than the other way around
#           - that means modifying the current setup of the UI initializer
#           - that also means that Game class won't get player in the __init__ but at some point later
#       Create GameManager class that will keep track of scores and create the necessary class instances
#           - Create player and game instances inside GameManager
#           - Remove player creation/selection functionality from the Game class
#       UI class has display_board and display_current_board methods. Is the second one needed?
#       Write unit tests
#       Start running the code to debug

from game_manager import GameManager

def main() -> None:
   gm = GameManager()
   gm.run() 

if __name__ == '__main__':
   main()