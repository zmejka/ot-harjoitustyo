
class Player:

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
