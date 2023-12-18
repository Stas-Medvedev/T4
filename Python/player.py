import random
from interfaces import Board

# TODO: One of Hard CPU turn functions returns a None. Needs to be fixed.
#       - Add unit tests for this (Installed pytest and pytest-cov. Upgraded to Python 3.11.3)

class Player:
    '''
    Player class for human player.
    '''
    def __init__(self, name: str, marker:str) -> None:
        self.name = name
        self.marker = marker

    def take_turn(self, board: Board) -> int:
        available_positions_strings = [str(position) for position in board.available_positions]
        position = input(f"{self.name}'s turn. Select a position {board.available_positions}: ")
        while position not in available_positions_strings:
            position = input(f"{self.name}'s turn. Select a position {board.available_positions}: ")
            
        return int(position)

class Easy_CPU_Player(Player):
    '''
    Easy CPU player selects an available space at random
    '''
    def take_turn(self, board: Board) -> int:
        return random.choice(board.available_positions)

class Hard_CPU_Player(Player):
    '''
    Hard CPU player follows an algorithm to make sure to not lose a game
    '''
    WINNING_POSITIONS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def can_win(self, board: Board) -> int:
        '''
        Checks if it's possible to win with the next move.
        If so, returns the position. Otherwise returns 0.
        '''
        for positions in self.WINNING_POSITIONS:
            total = 0
            for position in positions:
                current_position = board.markers[position]
                # if there's an opponent's marker in the current winning position,
                # move on to the next winning position
                if current_position != self.marker and current_position != ' ':
                    can_win = False
                    break
                if current_position == self.marker: total += 1
                if current_position == ' ':
                    blank = position
                    can_win = True
            if total == 2 and can_win: 
                return blank + 1
        return 0

    def need_to_cover(self, board: Board) -> int:
        '''
        Checks if the opponent could win with the next move.
        If so, returns the position that needs to be covered.
        Otherwise returns 0.
        '''
        for positions in self.WINNING_POSITIONS:
            total = 0
            for position in positions:
                current_position = board.markers[position]
                if current_position != self.marker and current_position != ' ':
                    total += 1
                if current_position == ' ': blank = position
            if total == 2: return blank + 1
        return 0

    def check_marker(self, marker: str, own: bool = True) -> bool:
        '''
        Checks whether the passed marker is own (when own=True)
        or an opponent's marker.
        Used in can_fork.
        '''
        if own:
            return marker == self.marker

        return marker not in [self.marker, ' ']

    def can_fork(self, own: bool, board: Board) -> int:
        '''
        Checks if it's possible to have two sets of positions that could win 
        on the following turn since the opponent can cover only one of them.
        For example, in the following scenario,
        
         | |O  
        -+-+-  
        O|X|    
        -+-+-  
        X| |   

        placing an 'X' in position 3 (bottom right) would 'fork'
        by giving the opponent two positions to cover (2 and 7)
        on the next move.
        
         | |O  
        -+-+-  
        O|X|   
        -+-+-  
        X| |X   

        own=True checks own forks. own=False checks for opponent's forks.
        '''
        # collect winning positions with an appropriate marker and two spaces
        candidates = []
        for positions in self.WINNING_POSITIONS:
            current_candidate = []
            add_to_list = True
            for position in positions:
                current_position = board.markers[position]
                # if current position is an opposite marker, we can't fork,
                # so move on to the next set of winning positions
                if self.check_marker(current_position, not own):
                    # need a boolean in case the first two positions in the winning position
                    # are spaces and the last one is an opposite marker
                    add_to_list = False
                    break
                # storing only the positions of spaces
                if current_position == ' ': current_candidate.append(position)
            # save only positions with 2 spaces
            if len(current_candidate) == 2 and add_to_list: candidates.append(current_candidate)

        # we need at least 2 candidates to be able to fork
        if len(candidates) < 2: return 0

        # use a double loop to compare all candidates to each other
        # and return the first intersecting empty space
        for i in range(len(candidates)-1):
            for j in range(i+1, len(candidates)):
                current_candidate = candidates[i]
                compared_candidate = candidates[j]
                for position in current_candidate:
                    if position in compared_candidate:
                        return position + 1

        # if loop returns no intersections, return 0
        return 0

    def take_corner_or_side(self, board: Board) -> int:
        '''
        Take a corner based on logic. If none available, take a side.
        '''
        # If take_turn gets to this function, the center has already been taken.
        # Start by looking at the number of available positions.
        # If there are 8 (only 1 is taken), the taken space is the center,
        # so take any of the corners
        corner_positions = [1, 3, 7, 9]
        random.shuffle(corner_positions)
        if len(board.available_positions) == 8: return corner_positions[0]
        # If there are 7 available positions, it means we have the center
        # and the opponent has the other position.
        # The square we should take up depends on what the opponent took.
        if len(board.available_positions) == 7:
            # If the opponent took a corner, place a marker in the opposite corner
            # to try to get a mistake.
            opp_positions = {1:9, 3:7, 7:3, 9:1}
            for key in opp_positions.keys():
                if self.check_marker(board.available_positions[key], own=False):
                    return opp_positions[key]
            # For any other position, return a corner.
            return corner_positions[0]
        # if 3 or more positions have been taken, other functions should be able to cover
        # most cases, so this function should run through corners and then sides,
        # and return one of them (this will need to be tested) 
        for corner in corner_positions:
            if corner in board.available_positions: return corner
        
        sides = [2, 4, 6, 8]
        random.shuffle(sides)
        for side in sides:
            if side in board.available_positions: return side

    def check_diagonal_case(self, board: Board) -> int:
        '''
        Checks a special case when going second on second turn (4th turn overall).
        
        In cases
        
         | |X      X| |
        -+-+-      -+-+-  
         |O|   or   |O|
        -+-+-      -+-+- 
        X| |        | |X,

        can_fork function would place a marker in one of the available corners,
        and that would lead to a loss. The correct move is to place a marker on
        one of the available sides.
        '''
        # if any of the following conditions are not met, this case doesn't apply:
        # there are exactly 6 avaliable positions, 
        # the center position has an own marker,
        # either of the corner combinations have opponent's markers
        if len(board.available_positions) != 6: return 0
        if not self.check_marker(board.markers[4], own=True): return 0
        
        corner_1 = self.check_marker(board.markers[0], own=False)
        corner_9 = self.check_marker(board.markers[8], own=False)
        corner_3 = self.check_marker(board.markers[3], own=False)
        corner_7 = self.check_marker(board.markers[6], own=False)
        if (corner_1 and corner_9) or (corner_3 and corner_7):
            sides = [2, 4, 6, 8]
            return random.choice(sides)

        return 0
    
    def take_turn(self, board: Board) -> int:
        '''
        Can win: a winning position with 2 own markers and an empty space
        Need to cover: a winning position with 2 of opponent's markers and an empty space
        Can fork: two winning positions that have an own marker each and an intersecting empty space

        If center is available, take that.
        If can win, choose the remaining empty space.
        If need to cover, choose the remaining empty space.
        Check the special diagonal case when going second.
        If can fork, choose the intersecting space.
        If opponent can fork on next move, block the fork.
        Pick a corner space (this will probably need hardcoded values)
        Pick a side space
        '''
        strategy_count = 1
        print(f'Strategy: {strategy_count}')
        if 5 in board.available_positions: return 5

        move_strategies = [self.can_win, self.need_to_cover, self.check_diagonal_case]
        for strategy in move_strategies:
            strategy_count += 1
            position = strategy(board)
            print(f'Strategy: {strategy_count}')
            if position: return position
        # position = self.can_win()
        # if position: return position
        # position = self.need_to_cover()
        # if position: return position
        # position = self.check_diagonal_case
        # if position: return position
        for own in [True, False]:
            strategy_count += 1
            position = self.can_fork(own=own, board=board)
            print(f'Strategy: {strategy_count}')
            if position: return position

        return self.take_corner_or_side(board)
        

class Medium_CPU_Player(Hard_CPU_Player):
    '''
    Medium CPU player randomly chooses between Easy and Hard CPU players' moves
    '''
    def take_turn(self, board: Board) -> int:
        move_choice = random.choice([0,1])
        if move_choice == 0:
            return random.choice(board.available_positions)
        else:
            super().take_turn(board)