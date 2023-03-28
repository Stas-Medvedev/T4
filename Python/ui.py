class UI:
    
    @staticmethod
    def get_player_selection() -> tuple[str, str]:
        '''
        Prompts the user to make a player type selection, and returns a tuple of player types
        that is used to generate the appropriate player objects.
        '''
        player_pairs = {'1': ("human", "human"), '2': ("human", "cpu"), '3': ("cpu", "human")}
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