import random
import itertools
from objects.ship import Ship

class Board:
    ''' Arguments:
        board : 10x10 zero-matrix.
        ships : list on ship objects.
        game_status : if "True" game is over.
        ammo : number of ammo. In single game - 40. In PvC game - 100.
        coordinates : list of tuples (row, column) of the all cells in matrix
    '''

    def __init__(self):
        self.board = [[0]*10 for i in range(10)]
        self.ships = []
        self._game_status = False
        self._ammo = 45
        self._coordinates = []
        for row, col in itertools.product(range(10), range(10)):
            self._coordinates.append((row,col))
        self.notices = []

    def create_ships(self):
        ''' Creating 5 types of ships with random orientation and
            adding to ships-list.
            Used in single game and PvC game to create computer ships.
            Ships are added to the ships-list.
        '''
        self.ships.append(Ship("Lentotukialus", 5, int(random.randint(0,1))))
        self.ships.append(Ship("Taistelulaiva", 4, int(random.randint(0,1))))
        self.ships.append(Ship("Risteilijä", 3, int(random.randint(0,1))))
        self.ships.append(Ship("Sukellusvene", 3, int(random.randint(0,1))))
        self.ships.append(Ship("Hävittäjä", 2, int(random.randint(0,1))))

    def randomize_ships(self):
        ''' Randomily draw the coordinates for each ship in the list
            and try to place ship on board.
        '''
        for i in self.ships:
            location = False
            while not location:
                coordinates = i.ship_random_position()
                if self.place_the_ship(i, coordinates, i.get_orientation(), i.get_length()):
                    location = True

    def place_the_ship(self, ship, coordinates, orientation, length):
        ''' Checking that the ship can fit in the gameboard and add coordinates to the list.
            Args:
                coordinates : pair of numbers. Both of coordinates are random number between 0-9
                orientation : orintation of the ship
                length : length of the ship
            Returns:
                True, if ship fit in the gameboard
                False, if ship do not fit in the gameboard
        '''
        if orientation == 1 and coordinates[0]+length < 11:
            if self._overlap_check(coordinates, orientation, length):
                for i in range(length):
                    self.board[coordinates[0]+i][coordinates[1]]=1
                    place = (coordinates[0]+i, coordinates[1])
                    ship.position.append(place)
                return True
        if orientation == 0 and coordinates[1]+length < 11:
            if self._overlap_check(coordinates, orientation, length):
                for i in range(length):
                    self.board[coordinates[0]][coordinates[1]+i]=1
                    place = (coordinates[0], coordinates[1]+i)
                    ship.position.append(place)
                return True
        return False

    def _overlap_check(self, coordinates, orientation, length):
        ''' Checking that the ship do not overlay other ships.
        Args:
            coordinates : pair of numbers. Both of coordinates are random number between 0-9
            orientation : orintation of the ship
            length : length of the ship
        Returns:
            True, if ship no overlap any ship
            False, if ship overlap other ship
        '''
        if orientation == 1:
            for i in range(length):
                if self.board[coordinates[0]+i][coordinates[1]]==1:
                    return False
        if orientation == 0:
            for i in range(length):
                if self.board[coordinates[0]][coordinates[1]+i]==1:
                    return False
        return True

    def shot(self, row, col):
        ''' Shooting to the board.
            If player have at least 1 ammo, check cell value on board.
            Remove 1 ammo and perform ship_check.
            Args:
                row : row in matrix
                col : column in matrix
            Returns:
                True, if board has been shot.
                False, if player has no ammunition
        '''
        if self._ammo > 0:
            if self.board[row][col] < 2:
                hit = (row, col)
                self.board[row][col] = self.board[row][col] + 2
                self._ship_check(hit)
            self._ammo = self._ammo - 1
            return True
        self._game_status = True
        return False

    def comp_shot(self):
        ''' Randomly draw coordinates from the list of coordinates.
            Shoot at the given location and remove the coordinates from the list.
            Returns:
                pair of coordinates (row, column)
        '''
        random_coordinates = random.choice(self._coordinates)
        self.shot(random_coordinates[0], random_coordinates[1])
        self._coordinates.remove(random_coordinates)
        return random_coordinates

    def _ship_check(self, coordinates):
        ''' If pair of coordinates in ship's list, add hit.
            Args:
                coordinates : pair of numbers. Both of coordinates are random number
                between 0-9.
        '''
        if self.board[coordinates[0]][coordinates[1]] == 3:
            for ship in self.ships:
                if coordinates in ship.position:
                    ship.add_hit()
                    self._notification(ship)

    def _notification(self, ship):
        ''' Checking if ships are sunk and add notification to notification list. '''
        if ship.are_sunk():
            self.notices.append(ship.get_notice())

    def _check_game_over(self):
        ''' Checking for game status. If all 5 ships are sunk, set game status to
            True.
            Args:
                counter for sunken ships. 0 at start.
            Returns:
                game_status.'''
        counter = 0
        for ship in self.ships:
            if ship.are_sunk():
                counter = counter + 1
        if counter == 5:
            self._game_status = True

    def game_over(self):
        ''' Checkingif game is over.
            Returns:
                True, if game is over.
                False, if game continue.
        '''
        self._check_game_over()
        if self._game_status:
            return True
        return False

    def set_ammo(self, ammo):
        ''' For PvC game: Set number of ammo to given number.
            Args:
                ammo : number of the ammunition
        '''
        if isinstance(ammo, int):
            self._ammo = ammo

    def get_ammo(self):
        ''' Returns:
            number of ammunition.'''
        return self._ammo
