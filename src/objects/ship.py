import random

class Ship:

    ''' Arguments:
        name : string.
        length : int, length of the ship between 2 - 5.
        orientation : 1 = vertical, 0 = horizontal.
        status : if "True" ship are sunk.
        position : list of coordinates (row,column) of the ship.
        hits : counter for hits.
        notice : string, notification of the ship status.
    '''

    def __init__(self, name, length, orientation):
        self._name = name
        self._length = length
        self._orientation = orientation
        self._status = False
        self.position = []
        self._hits = 0
        self._notice = ""

    def get_name(self):
        ''' Returns:
                name of the ship. '''
        return self._name

    def get_notice(self):
        ''' Returns:
                ship notice.
        '''
        return self._notice

    def get_length(self):
        ''' Returns:
                length of the ship. '''
        return self._length

    def get_orientation(self):
        ''' Returns:
                orientation of the ship. '''
        return self._orientation

    def _set_status(self, status):
        ''' Set status of the ship if it's True or False.
            Args:
            status : boolean, status of the ship
        '''
        if status in (True, False):
            self._status = status

    def are_sunk(self):
        ''' Returns:
                status of the ship. '''
        return self._status

    def ship_random_position(self):
        ''' Returns:
            pair of the random coordinates.
            Both of coordinates are random number between 0-9.'''
        return int(random.randint(0,9)), int(random.randint(0,9))

    def add_hit(self):
        ''' Add 1 to the counter of the hits.
            If number of the hits is equal to length of the ship,
            set ship status to True (ship are sunk).'''
        self._hits = self._hits + 1
        if self._hits == self._length:
            self._notice = self._name + " on uponnut!"
            self._set_status(True)
     