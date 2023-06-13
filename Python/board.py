from collections import Counter

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

        # Take the rows in the reverse order because the first row is 
        # at the end of the input string and skip the separator rows 
        board_string = board_string.split('\n')
        board_string = board_string[-1::-2]

        # Check to make sure rows have the correct number of characters
        for i in range(len(board_string)):
            if len(board_string[i]) > 5: raise ValueError(f"Too many characters in row {i+1}")
            if len(board_string[i] < 5): raise ValueError(f"Not enough characters in row {i+1}")

        # Add '|' to join rows so that all characters are separated by the same character
        # It makes splitting in the next step easier
        board_string = '|'.join(board_string)
        markers = board_string.split('|')

        # TODO: Add a check to make sure that there are no more than two 
        # markers and spaces and that the numbers of spaces occupied by each
        # marker are within one of each other
        marker_counter = Counter(markers)
        key_list = list(marker_counter.keys())
        # TODO:
        # Make sure there are 3 or fewer keys in the counter
        if len(key_list) > 3:
            raise ValueError('Too many markers')
        # If there is only one key, make sure it's the space
        if len(key_list) == 1 and ' ' not in key_list:
            raise ValueError('Invalid board: only 1 marker')
        # If there are two keys, and space is one of them, make sure count for space is 8
        if len(key_list) == 2:
            if ' ' in key_list:
                if marker_counter[' '] != 8:
                    raise ValueError('Invalid board: only one marker passed, and it appears too many times')
        # If there are two keys, and space is not one of them,
        # make sure the counts for the markers are 5 and 4
            else: # if ' ' not in key_list
                pass # add check
        # If there are three keys, make sure that the counts 
        # for the markers that are not space are within one of each other 


        available_positions = [i+1 for i in range(9) if markers[i]==' ']
        # Add the above to a Board object
        board = cls()
        board.available_positions = available_positions
        board.markers = markers
        
        return board