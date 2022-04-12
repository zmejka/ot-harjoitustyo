#import time
#import pygame
from board import Board
#from game_board import GameBoard
#from game_loop import GameLoop
#from sprites.sea import Sea

CELL = 35

def main():
    board = Board()
    board.random_ships()
    board.initialize_ships()
    board.print_board()

    '''pygame.init()
    board = Board()
    game_board = GameBoard(board, cell)
    height = 20
    width = 40
    screen_height = height*CELL
    screen_width = width*CELL
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = (151,210,203)
    sea = Sea(50,50)

    screen.fill(background)
    pygame.display.update()
    pygame.display.set_caption("BattleShip")
    all_sprites = pygame.sprite.Group()
    all_sprites.add(sea)

    game_loop = GameLoop(game_board, cell)
    game_loop.start()
    abort_time = 20
    start = time.time()
    while True:
        break_time = time.time() - start
        pygame.display.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        if break_time >= abort_time:
            break
        game_board.all_sprites.draw(screen) '''


if __name__ == "__main__":
    main()
