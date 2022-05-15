import pygame
from assets.image import image

class Battleship(pygame.sprite.Sprite):
    def __init__(self, x_axis, y_axis):
        super().__init__()

        self.image = image("battleship.png")

        self.rect = self.image.get_rect()
        self.rect.topleft = (x_axis,y_axis)
