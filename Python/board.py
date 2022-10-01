class Board:
    available_positions = list(range(1,10))
    current_markers = [' '] * 9

    def display_board(self):
        '''
        Displays the playing grid.
        '''
        row1 = "|".join(x for x in self.current_markers[:3])
        row2 = "|".join(x for x in self.current_markers[3:6])
        row3 = "|".join(x for x in self.current_markers[6:])
        row_separator = '-+-+-'
        print()
        print(row3)
        print(row_separator)
        print(row2)
        print(row_separator)
        print(row1)
        print()

    def display_instructions(self):
        '''
        Displays instructions and the cell numbers.
        '''
        print('Classic tic-tac-toe. To play, select a position number to place your marker according to the grid below')
        self.display_grid([str(x) for x in self.available_positions])

    def update_grid(self, position, marker):
        '''
        Updates the current_positions list to include the most recent marker
        and removes the recent position from available_positions.
        '''
        self.current_markers[position - 1] = marker
        self.available_positions.remove(position)