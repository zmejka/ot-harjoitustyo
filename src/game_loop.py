import pygame

class GameLoop:
    def __init__(self, game_board, cell):
        self._game_board = game_board
        self._cell = cell

    def start(self):
        while True:
            if not self._event():
                break

    def _event(self):
        return True
        