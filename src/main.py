import os
import sys
import pygame
from objects.board import Board
from results import Results
from ui.menu import Menu
from ui.single import Single
from ui.pvc import PvC
from ui.scores import Scores

CELL = 37
WIDTH = 37
HEIGHT = 20
FPS = 50

dirname = os.path.dirname(__file__)

class Main:
    ''' Args:
        width : screen width in pixels
        height : screen height in pixels
    '''
    def __init__(self):
        self._width = WIDTH*CELL
        self._height = HEIGHT*CELL

    def main(self):
        ''' Note: In rows (32) pygame.init and (50, 55) pygame.quit: pylint: disable=no-member!
            Args:
                Initializing pygame and creating screen.
                menu : menu object
                all_sprites : list of the all sprites
                start game loop
        '''
        pygame.init() # pylint: disable=no-member
        screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("BattleShip")
        menu = Menu(screen, self._width, self._height)
        all_sprites = pygame.sprite.Group()
        self.game_loop(screen, menu, all_sprites)
        pygame.sys.exit()

    def game_loop(self, screen, menu, all_sprites):
        ''' Main menu loop:
            Single : start single game
            PvC : start player vs computer game
            Results : show results of previous games
            Quit : game exit
        '''
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # pylint: disable=no-member
                    raise SystemExit
                if menu.menu() == "Quit":
                    pygame.quit() # pylint: disable=no-member
                    sys.exit()
                if menu.menu() == "Single":
                    single = self.start_single(screen)
                    single.single_game()
                if menu.menu() == "PvC":
                    pl_vs_comp = self.start_pvc(screen)
                    pl_vs_comp.initialize()
                if menu.menu() == "Scores":
                    self.result_list()
                    scores = Scores(screen, self._width, self._height)
                    scores.scores(self.result_list())
            pygame.display.update()
            all_sprites.draw(screen)
            pygame.display.flip()

    def start_single(self, screen):
        ''' Initialize single game.
            Args:
                board : board object
                create ships : create 5 ship objects
                randomize ships : randomly place 5 ships on board
                single : single game object
            Returns:
                single object
        '''
        board = Board()
        board.create_ships()
        board.randomize_ships()
        single = Single(screen,WIDTH*CELL, HEIGHT*CELL, board)
        return single

    def start_pvc(self, screen):
        ''' Initialize player vs computer game.
            Args:
                player_board and comp_board : board objects for player and ai.
                set_ammo : sets both board ammonition number to 100.
                create_ships : create 5 ship objects for ai
                randomize_ships : randomly place 5 ships on comp_board
                pl_vs_comp : PvC game object
            Returns:
                pl_vs_comp object
        '''
        player_board = Board()
        player_board.set_ammo(100)
        comp_board = Board()
        comp_board.set_ammo(100)
        comp_board.create_ships()
        comp_board.randomize_ships()
        pl_vs_comp = PvC(screen,WIDTH*CELL, HEIGHT*CELL, player_board, comp_board)
        return pl_vs_comp

    def result_list(self):
        ''' Load results from the results_file.
            Trim each row and change score from strin to integer.
            Sort the list.
            Args:
                results : results object
                result_list : list of the results loaded from the file
            Returns:
                3 best results in list (player, score)
        '''
        results = Results()
        result_list = results.load_results()
        if not result_list:
            return None
        score_list = []
        for row in result_list:
            values = row[:-1].split(',')
            score_list.append((values[0], int(values[1])))
        score_list = sorted(score_list, key=lambda x:x[1], reverse=False)
        return score_list[0:3]
