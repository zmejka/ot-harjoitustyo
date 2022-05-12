import unittest
import pygame
from main import Main
from ui.menu import Menu
from ui.single import Single
from ui.pvc import PvC

class TestShip(unittest.TestCase):
    def setUp(self):
        self.main = Main()
        CELL = 3
        WIDTH = 50
        HIGHT = 50
        self.width = CELL*WIDTH
        self.hight = CELL*HIGHT

    def test_main(self):
        self.assertEqual(self.width, 150)
        self.assertEqual(self.hight, 150)

    def test_main_menu(self):
        pygame.init()
        test_screen = pygame.display.set_mode((self.width, self.hight))
        test_menu = Menu(test_screen, self.width, self.hight)
        self.assertIsInstance(test_menu, Menu)
    
    def test_menu_single(self):
        pygame.init()
        test_screen = pygame.display.set_mode((self.width, self.hight))
        self.assertIsInstance(self.main.start_single(test_screen), Single)
    
    def test_menu_not_pvc(self):
        pygame.init()
        test_screen = pygame.display.set_mode((self.width, self.hight))
        self.assertNotIsInstance(self.main.start_single(test_screen), PvC)

    def test_menu_pvc(self):
        pygame.init()
        test_screen = pygame.display.set_mode((self.width, self.hight))
        self.assertIsInstance(self.main.start_pvc(test_screen), PvC)
    
    def test_menu_not_single(self):
        pygame.init()
        test_screen = pygame.display.set_mode((self.width, self.hight))
        self.assertNotIsInstance(self.main.start_pvc(test_screen), Single)        

