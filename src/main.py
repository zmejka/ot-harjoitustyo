import pygame
from objects.board import Board
from ui.menu import Menu
from ui.single import Single
from ui.pvc import PvC

CELL = 37
WIDTH = 37
HEIGHT = 20
FPS = 50

def main():
    ''' Arguments:
    screen_height = hight of the screen in pixels.
    screen_width = width of the screen in pixels
    - Initialize game window
    - Initialize sprites
    - Game loop:
        Initialize Single game
        Initialize Player vs Computer game
        Quit the game
    '''

    screen_height = HEIGHT*CELL
    screen_width = WIDTH*CELL

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BattleShip")
    menu = Menu(screen, screen_width, screen_height)

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
                player_board = Board()
                player_board.set_ammo(100)
                comp_board = Board()
                comp_board.set_ammo(100)
                comp_board.create_ships()
                comp_board.randomize_ships()
                pl_vs_comp = PvC(screen,screen_width, screen_height, player_board, comp_board)
                pl_vs_comp.pvc_game()

            if menu.menu() == "Quit":
                pygame.sys.exit()

        pygame.display.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.sys.exit()

if __name__ == "__main__":
    main()
