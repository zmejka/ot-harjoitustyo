from ship import Ship
import random

class Board:

    def __init__(self):
        self.board = [['0']*10]*10
        self.visible = True
        self.ships = []

    def placeTheShip(self, ship):
        name = ship.getName()
        length = ship.getLenght()
        orientation = ship.getOrientation()
        sunk = False

    def shipPosition(self):
        letters = ['A','B','C','D','E','F','G','H','I','J']
        return random.choice(letters), int(random.randint(0,10))

    def printBoard(self):
        for i in self.board:
            print (i)






