import pygame
from assets.image import image

class CruiserVert(pygame.sprite.Sprite):
    def __init__(self, x_axis, y_axis):
        super().__init__()

        self.image = image("cruiser_vert.png")

        self.rect = self.image.get_rect()
        self.rect.topleft = (x_axis,y_axis)
