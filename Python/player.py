import random

class Player:
    '''
    Player class for human player.
    '''
    
    def __init__(self, name, marker, board):
        self.name = name
        self.marker = marker
        self.board = board

    def take_turn(self):
        position = int(input(f"{self.name}'s turn. Select a position {self.board.available_positions}:"))
        return position

class Easy_CPU_Player(Player):
    '''
    Easy CPU player selects an available space at random
    '''
    def take_turn(self):
        return random.choice(self.board.available_positions)

class Hard_CPU_Player(Player):
    '''
    Hard CPU player follows an algorithm to make sure to not lose a game
    '''
    WINNING_POSITIONS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    # This class needs access to the game board

    def can_win(self):
        '''
        Checks if it's possible to win with the next move.
        If so, returns the position. Otherwise returns 0.
        '''
        for positions in self.WINNING_POSITIONS:
            total = 0
            for position in positions:
                if self.board.current_positions[position] == self.marker: total += 1
                if self.board.current_positions[position] == ' ': blank = position
            if total == 2: return blank + 1
        return 0

    def need_to_cover(self):
        '''
        Checks if the opponent could win with the next move.
        If so, returns the position that needs to be covered.
        Otherwise returns 0.
        '''
        for positions in self.WINNING_POSITIONS:
            total = 0
            for position in positions:
                current_position = self.board.current_positions[position]
                if current_position != self.marker and current_position != ' ':
                    total += 1
                if current_position == ' ': blank = position
            if total == 2: return blank + 1
        return 0

    def can_fork(self):
        '''
        Checks if it's possible to have two sets of positions that could win 
        on the following turn since the opponent can cover only one of them.
        '''
        '''
        Check if a winning position has two empty spaces.
        If it does, check if there's another winning position that contains either
        of the two spaces and one marker.
        '''
        pass
    
    def take_turn(self):
        '''
        Can win: a winning position with 2 own markers and an empty space
        Need to cover: a winning position with 2 of opponent's markers and an empty space
        Can fork: two winning positions that have an own marker each and an intersecting empty space

        If center is available, take that.
        If can win, choose the remainng empty space.
        If need to cover, choose the remaining empty space.
        If can fork, choose the intersecting space.
        Pick a space from a winning position that already has one own marker,
        this will require the opponent to cover, make sure that the opponent can't fork with the cover.
        Pick a random space. (will probably only be used one the first turn if center is unavailable)
        '''
        if 5 in self.board.available_positions: return 5

class Medium_CPU_Player(Hard_CPU_Player):
    '''
    Medium CPU player randomly chooses between Easy and Hard CPU players' moves
    '''
    def take_turn(self):
        move_choice = random.choice([0,1])
        if move_choice == 0:
            return random.choice(self.board.available_positions)
        else:
            super().take_turn()