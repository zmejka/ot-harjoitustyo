import random

class Ship:

    ''' Arguments:
    name = string.
    length = int, length of the ship between 2 - 5.
    orientation: 1 = vertical, 0 = horizontal.
    game_status = if "True" ship are sunk.
    position = coordinates (row,column) of the bow of the ship  '''

    def __init__(self, name, length, orientation):
        self.name = name
        self.length = length
        self.orientation = orientation
        self.status = False
        self.position = (0,0)

    def set_name(self, shipname):
        self.name = shipname

    def get_name(self):
        return self.name

    def set_length(self, length):
        if length > 0:
            self.length = length

    def get_length(self):
        return self.length

    def set_orientation(self, orientation):
        self.orientation = orientation

    def get_orientation(self):
        return self.orientation

    def set_status(self, status):
        self.status = status

    def are_sunk(self):
        return self.status

    def ship_position(self):
        return int(random.randint(0,9)), int(random.randint(0,9))
