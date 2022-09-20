import random

class Player:
    '''
    Player class for human player.
    '''
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def take_turn(self, available_positions):
        position = int(input(f"{self.name}'s turn. Select a position {available_positions}:"))
        return position

class Easy_CPU_Player(Player):
    '''
    Easy CPU player selects an available space at random
    '''
    def take_turn(self, available_positions):
        return random.choice(available_positions)

class Medium_CPU_Player(Player):
    '''
    Medium CPU player randomly chooses between Easy and Hard CPU players' moves
    '''
    def take_turn(self, available_positions):
        move_choice = random.choice([0,1])
        if move_choice == 0:
            self.easy_turn(available_positions)
        else:
            self.hard_turn(available_positions)

    def easy_turn(self, available_positions):
        return random.choice(available_positions)

    def hard_turn(self, available_positions):
        pass

class Hard_CPU_Player(Player):
    '''
    Hard CPU player follows an algorithm to make sure to not lose a game
    '''
    def take_turn(self, available_positions):
        '''
        Can win: a winning position with 2 own markers and an empty space
        Need to cover: a winning position with 2 of opponent's markers and an empty space
        Can fork: two winning positions that have an own marker each and an intersecting empty space

        If center is available, take that.
        If can win, choose the remainng empty space.
        If need to cover, choose the remaining empty space.
        If can fork, choose the intersecting space.
        Pick a space from a winning position with that already has one own marker,
        this will require the opponent to cover, make sure that the opponent can't fork with the cover.
        Pick a random space. (will probably only be used one the first turn if center is unavailable)
        '''
        pass