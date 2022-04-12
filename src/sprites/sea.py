import pygame
from image import image

class Sea(pygame.sprite.Sprite):
    def __init__(self, x_axis=0, y_axis=0):
        super().__init__()

        self.image = image("board.png")

        self.rect = self.image.get_rect()
        self.rect.center = (300,300)
