class Board:
    available_positions = list(range(1,10))
    markers = [' '] * 9

    def update(self, position: int, marker: str) -> None:
        '''
        Updates the board with the most recent marker.
        '''
        self.markers[position - 1] = marker
        self.available_positions.remove(position)