class Player:
    ''' Arguments:
        name : string.
        status : turn status of the player.
            If "True" is player's turn.
    '''

    def __init__(self, name, status):
        self._name = name
        self._status = status

    def get_name(self):
        ''' Returns:
                name of the player
        '''
        return self._name

    def set_name(self, name):
        ''' Set name of the player. There are no limitations for player name,
            except length has to be in between 3 - 39 symbols.
            Args:
                name : string
            Returns:
                True if name are setted
                False if name are to short
        '''
        if len(name) > 2 and len(name) < 40:
            self._name = str(name)
            return True
        return False

    def set_status(self, status):
        ''' Change status of the player. '''
        if isinstance(status, bool):
            self._status = status

    def get_status(self):
        ''' Returns:
            Status of the player.
        '''
        return self._status
