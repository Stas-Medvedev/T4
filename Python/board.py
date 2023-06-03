class Board:
    '''
    Class to hold the information on filled markers and available
    spaces for the current game.
    '''

    def __init__(self):
        self.available_positions = list(range(1,10))
        self.markers = [' '] * 9

    def update(self, position: int, marker: str) -> None:
        '''
        Updates the board with the most recent marker.
        Position is a number between 1 and 9, hence (position - 1)
        is used for indexing.
        '''
        self.markers[position - 1] = marker
        self.available_positions.remove(position)

    @classmethod
    def from_string(cls, board_string: str) -> 'Board':
        '''
        Converts a multiline string representation of a board into a Board object
        '''
        # Validate string fomat
        # Split the string on new line
        # Take entries 4, 2, and 0
        # Split those on the pipe character
        # Combine and move all to the markers array
        # Add empty spaces to the available_positions array
        board_string = board_string.split('\n')
        board_string = board_string[-1::-2]

        # check to make sure rows have the correct number of characters
        for i in range(len(board_string)):
            if len(board_string[i]) > 5: raise ValueError(f"Too many characters in row {i+1}")
            if len(board_string[i] < 5): raise ValueError(f"Not enough characters in row {i+1}")

        board_string = '|'.join(board_string)
        markers = board_string.split('|')
        available_positions = [i+1 for i in range(9) if markers[i]==' ']
        # Add the above to a Board object
        board = cls()
        board.available_positions = available_positions
        board.markers = markers
        
        return board