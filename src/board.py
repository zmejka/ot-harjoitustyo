import random
from ship import Ship

class Board:

    def __init__(self):
        self.board = [[0]*10 for i in range(10)]
        self.visible = True
        self.ships = []
        self.game_status = False

    def random_ships(self):
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

    def ship_position(self):
        #letters = ['A','B','C','D','E','F','G','H','I','J']
        #random.choice(letters)
        return int(random.randint(0,9)), int(random.randint(0,9))

    def initialize_ships(self):
        for i in self.ships:
            location = False
            while not location:
                coordinates = self.ship_position()
                location = self.place_the_ship(coordinates, i.get_orientation(), i.get_length())

    def place_the_ship(self, coordinates, orientation, length):
        if orientation == 1 and coordinates[0]+length < 9:
            for i in range(length):
                self.overlap_check(coordinates, orientation, length)
                self.board[coordinates[0]+i][coordinates[1]]=1
            return True
        if orientation == 0 and coordinates[1]+length < 9:
            for i in range(length):
                self.overlap_check(coordinates, orientation, length)
                self.board[coordinates[0]][coordinates[1]+i]=1
            return True
        return False

    def overlap_check(self, coordinates, orientation, length):
        if orientation == 1:
            for i in range(length):
                if self.board[coordinates[0]+i][coordinates[1]]==1:
                    return False
            return True
        if orientation == 0:
            for i in range(length):
                if self.board[coordinates[0]][coordinates[1]+i]==1:
                    return False
            return True
        return False

    def print_board(self):
        for i in self.board:
            print (i)

    def game_over(self):
        return self.game_status
