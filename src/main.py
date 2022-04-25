import pygame
from board import Board
from ui.menu import Menu
from ui.single import Single
from ui.pvc import PvC

CELL = 37
WIDTH = 37
HEIGHT = 20
FPS = 50

def main():
    screen_height = HEIGHT*CELL
    screen_width = WIDTH*CELL

    # Initialize game window
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BattleShip")
    menu = Menu(screen, screen_width, screen_height)

    # Initialize sprites
    all_sprites = pygame.sprite.Group()

    game = True

    while game:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                game = False

            if menu.menu() == "Single":
                board = Board()
                board.create_ships()
                board.randomize_ships()
                single = Single(screen,screen_width, screen_height, board)
                single.single_game()

            if menu.menu() == "PvC":
                board = Board()
                board.create_ships()
                board.randomize_ships()
                pl_vs_comp = PvC(screen,screen_width, screen_height, board)
                pl_vs_comp.pvc_game()


            if menu.menu() == "Quit":
                pygame.sys.exit()

        pygame.display.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.sys.exit()

if __name__ == "__main__":
    main()
