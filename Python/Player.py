class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def take_turn(self, available_positions):
        position = int(input(f"{self.name}'s turn. Select a position {available_positions}:"))
        return position

class Easy_CPU_Player(Player):
    pass

class Medium_CPU_Player(Player):
    pass

class Hard_CPU_Player(Player):
    pass