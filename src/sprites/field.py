import pygame
from image import image

class Field(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image("board.png")
        self.rect = self.image.get_rect()
        self.rect.center = (300,300)
        