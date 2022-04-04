
class Ship:

    def __init__(self, name, length, orientation):
        self.name = name
        self.length = length
        self.orientation = orientation  #orientation: 1 = vertical, 0 = horizontal

    def setName(self, shipname):
        self.name = shipname

    def getName(self):
        return self.name

    def setLength(self, length):
        if length > 0:
            self.length = length

    def getLength(self):
        return self.length

    def setOrientation(self, orientation):
        self.orientation = orientation

    def getOrientation(self):
        return self.orientation

