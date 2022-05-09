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
        kirjoita uudestaan
    '''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH*CELL, HEIGHT*CELL))
    pygame.display.set_caption("BattleShip")
    menu = Menu(screen, WIDTH*CELL, HEIGHT*CELL)
    all_sprites = pygame.sprite.Group()
    game_loop(screen, menu, all_sprites)
    pygame.sys.exit()

def game_loop(screen, menu, all_sprites):
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if menu.menu() == "Single":
                single =start_single(screen)
                single.single_game()
            if menu.menu() == "PvC":
                pl_vs_comp = start_pvc(screen)
                pl_vs_comp.initialize()
            if menu.menu() == "Quit":
                pygame.sys.exit()
        pygame.display.update()
        all_sprites.draw(screen)
        pygame.display.flip()

def start_single(screen):
    board = Board()
    board.create_ships()
    board.randomize_ships()
    single = Single(screen,WIDTH*CELL, HEIGHT*CELL, board)
    return single

def start_pvc(screen):
    player_board = Board()
    player_board.set_ammo(100)
    #player_board.create_ships()
    #player_board.randomize_ships()
    comp_board = Board()
    comp_board.set_ammo(100)
    comp_board.create_ships()
    comp_board.randomize_ships()
    pl_vs_comp = PvC(screen,WIDTH*CELL, HEIGHT*CELL, player_board, comp_board)
    return pl_vs_comp

if __name__ == "__main__":
    main()
