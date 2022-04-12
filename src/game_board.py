import pygame
from sprites.sea import Sea

class GameBoard:
    def __init__(self, board, cell):
        self.cell = cell
        self.sea = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.board = board

        #clock = pygame.time.Clock()
        self._initialize_sprites(board)
        self.all_sprites.update()

    def _initialize_sprites(self, board):
        height = 10
        width = 10

        for i in range(height):
            for j in range(width):
                cell = board.board[i][j]
                norm_i = i * self.cell
                norm_j = j * self.cell

                if cell == 0:
                    self.sea.add(Sea(norm_i, norm_j))

        self.all_sprites.add(self.sea)
        