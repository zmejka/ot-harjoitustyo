import os
import pygame

dirname = os.path.dirname(__file__)

def image(name):
    return pygame.image.load(os.path.join(dirname, "assets", name))
    