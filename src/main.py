import pygame
from board import Board
from game_board import GameBoard
from game_loop import GameLoop
from sprites.sea import Sea

cell = 35

def main():
    pygame.init()
    board = Board()
    #game_board = GameBoard(board, cell)
    height = 15
    width = 15
    screen_height = height*cell
    screen_width = width*cell
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = (151,210,203)
    sea = Sea(50,50)

    screen.fill(background)
    pygame.display.update()
    pygame.display.set_caption("BattleShip")
    all_sprites = pygame.sprite.Group()
    all_sprites.add(sea)

    #game_loop = GameLoop(game_board, cell)
    #game_loop.start()

    while True:
        pygame.display.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        #game_board.all_sprites.draw(screen)



if __name__ == "__main__":
    main()
