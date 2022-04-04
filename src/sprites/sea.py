import pygame
from image import image

class Sea(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = image("sea.png")

        self.rect = self.image.get_rect()
        self.rect.center = (20,20)
        #self.rect.x = 50
        #self.rect.y = 50
