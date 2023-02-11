from interfaces import Board

'''
TODO:
    - Go through the functions and see if any of them need to be moved to the GameManager class
        - move get_cpu_player_object()
        - move get_human_player_object() and perhaps replace with get_player_name()
    - Check if any of the imports can be replaced with interfaces
    - This class gets a Board object as an attribute. Is that the right way to go about it
        or should only the necessary information be passed to the class methods?
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

    # Will probably be removed, and display_board will be used alone
    def display_current_board(self) -> None:
        '''
        Displays the current playing board.
        '''
        self.display_board(self.board.current_markers)