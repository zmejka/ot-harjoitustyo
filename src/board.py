import random
from ship import Ship

class Board:

    ''' Arguments:
    board = 10x10 zero-matrix.
    visibility = if "True" all ships are visible to player, else ships are not visible to player.
    ships = list on ship objects.
    game_status = if "True" game is over. '''

    def __init__(self):
        self.board = [[0]*10 for i in range(10)]
        self.visible = True
        self.ships = []
        self.game_status = False
        self.ammo = 40

    def create_ships(self):
        ''' Creating 5 types of ships with random oriantation and adding to ships-list. '''
        carrier = Ship("Carrier", 5, int(random.randint(0,1)))
        battle_ship = Ship("Battleship", 4, int(random.randint(0,1)))
        cruiser = Ship("Cruiser", 3, int(random.randint(0,1)))
        submarine = Ship("Submarine", 3, int(random.randint(0,1)))
        destroyer = Ship("Destroyer", 2, int(random.randint(0,1)))

        self.ships.append(carrier)
        self.ships.append(battle_ship)
        self.ships.append(cruiser)
        self.ships.append(submarine)
        self.ships.append(destroyer)

    def randomize_ships(self):
        ''' Randomize coordinates for ships and try to place ship on board. '''
        for i in self.ships:
            location = False
            while not location:
                coordinates = i.ship_position()
                if self.place_the_ship(coordinates, i.get_orientation(), i.get_length()):
                    i.position = coordinates
                    location = True

    def place_the_ship(self, coordinates, orientation, length):
        ''' Checking that the ship can fit in the gameboard. '''
        if orientation == 1 and coordinates[0]+length < 9:
            if self.overlap_check(coordinates, orientation, length):
                for i in range(length):
                    self.board[coordinates[0]+i][coordinates[1]]=1
                return True
        if orientation == 0 and coordinates[1]+length < 9:
            if self.overlap_check(coordinates, orientation, length):
                for i in range(length):
                    self.board[coordinates[0]][coordinates[1]+i]=1
                return True
        return False

    def overlap_check(self, coordinates, orientation, length):
        ''' Checking that the ship do not overlay other ships. '''
        if orientation == 1:
            for i in range(length):
                if self.board[coordinates[0]+i][coordinates[1]]==1:
                    return False
        if orientation == 0:
            for i in range(length):
                if self.board[coordinates[0]][coordinates[1]+i]==1:
                    return False
        return True

    def shot(self, var1, var2):
        ''' Shooting to the board. '''
        if self.ammo > 0:
            if self.board[var1][var2] < 2:
                self.board[var1][var2] = self.board[var1][var2] + 2
            self.ammo = self.ammo - 1
            return True
        return False

    def print_board(self):
        ''' Printing the board for testing. '''
        for i in self.board:
            print (i)

    def game_over(self):
        ''' Checking for game status.  '''
        counter = 0
        for i in range(10):
            for j in range(10):
                if self.board[i][j] == 3:
                    counter = counter + 1
        if counter == 17:
            print("Peli on päätynyt!!")
        return self.game_status
