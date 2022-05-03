import random

class Ship:

    ''' Arguments:
        name = string.
        length = int, length of the ship between 2 - 5.
        orientation: 1 = vertical, 0 = horizontal.
        status = if "True" ship are sunk.
        position = list of coordinates (row,column) of the ship.
        hits = counter for hits. '''

    def __init__(self, name, length, orientation):
        self.name = name
        self.length = length
        self.orientation = orientation
        self.status = False
        self.position = []
        self.hits = 0

    def set_name(self, shipname):
        ''' Set new name of the ship. '''
        self.name = shipname

    def get_name(self):
        ''' Returns name of the ship. '''
        return self.name

    def set_length(self, length):
        ''' Set length of the ship if it's between 2 - 5. '''
        if length in range(2, 6):
            self.length = length

    def get_length(self):
        ''' Returns length of the ship. '''
        return self.length

    def set_orientation(self, orientation):
        ''' Set orientation of the ship if it's 0 or 1.'''
        if orientation in (0, 1):
            self.orientation = orientation

    def get_orientation(self):
        ''' Returns orientation of the ship. '''
        return self.orientation

    def set_status(self, status):
        ''' Set status of the ship if it's True or False. '''
        if status in (True, False):
            self.status = status

    def are_sunk(self):
        ''' Returns status of the ship. '''
        return self.status

    def ship_position(self):
        ''' Returns pair of the random coordinates.
            Both of coordinates are random number between 0-9.'''
        return int(random.randint(0,9)), int(random.randint(0,9))

    def get_hits(self):
        ''' Returns value of counter of the hits. '''
        return self.hits

    def add_hit(self):
        ''' Add 1 to the counter of the hits.
            If number of the hits is equal to length of the ship,
            set ship status to True (ship are sunk).'''
        self.hits = self.hits + 1
        if self.hits == self.length:
            self.set_status(True)
            print(self.name, "on uponnut!")
 