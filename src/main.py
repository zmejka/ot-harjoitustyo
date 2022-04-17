import time
from image import image
import pygame
from board import Board
#from ship import Ship
from game_board import GameBoard
from game_loop import GameLoop
from sprites.carrier import Carrier
from sprites.field import Field
from sprites.hit import Hit
from sprites.miss import Miss
from sprites.submarine import Submarine
from sprites.submarine_vert import Submarine_vert
from sprites.carrier import Carrier
from sprites.carrier_vert import Carrier_vert
from sprites.battleship import Battleship
from sprites.battleship_vert import Battleship_vert
from sprites.cruiser import Cruiser
from sprites.cruiser_vert import Cruiser_vert
from sprites.destroyer import Destroyer
from sprites.destroyer_vert import Destroyer_vert


CELL = 35
WIDTH = 40
HEIGHT = 20
FPS = 50

def main():

    # Initialize board and ships
    board = Board()
    board.random_ships()
    board.initialize_ships()
    game_board = GameBoard(board, CELL)
    screen_height = HEIGHT*CELL
    screen_width = WIDTH*CELL
    game_field = Field()
    board.print_board()

    # Initialize game window
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BattleShip")
    
    background = (151,210,203)
    screen.fill(background)
    pygame.display.update()

    # Initialize sprites
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(game_field)
    game_board.all_sprites.draw(screen)
    for j in board.ships:
        name = j.get_name()
        coordinates = j.position
        orientation = j.get_orientation()
        x_axis = 133 + coordinates[0]*37
        y_axis = 133 + coordinates[1]*37
        if orientation == 1:
            if name == "Submarine":
                all_sprites.add(Submarine_vert(y_axis, x_axis))
            elif name == "Carrier":
                all_sprites.add(Carrier_vert(y_axis, x_axis))
            elif name == "Cruiser":
                all_sprites.add(Cruiser_vert(y_axis, x_axis))
            elif name == "Battleship":
                all_sprites.add(Battleship_vert(y_axis, x_axis))
            else:
                all_sprites.add(Destroyer_vert(y_axis, x_axis))
        else:
            if name == "Submarine":
                all_sprites.add(Submarine(y_axis, x_axis))
            elif name == "Carrier":
                all_sprites.add(Carrier(y_axis, x_axis))
            elif name == "Cruiser":
                all_sprites.add(Cruiser(y_axis, x_axis))
            elif name == "Battleship":
                all_sprites.add(Battleship(y_axis, x_axis))
            else:
                all_sprites.add(Destroyer(y_axis, x_axis))
            
    #game_loop = GameLoop(game_board, CELL)
    #game_loop.start()
    abort_time = 30
    start = time.time()

    game = True

    while game:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                game = False

            if i.type == pygame.MOUSEBUTTONDOWN:
                mouse_function = pygame.mouse.get_pressed()
                mouse_position = pygame.mouse.get_pos()
                if mouse_function[0]:
                    if game_field.rect.collidepoint(mouse_position):
                        if mouse_position[0] < 133 or mouse_position[1] < 133:
                            continue
                        elif mouse_position[0] > 502 or mouse_position[1] > 502:
                            continue
                        ylakulma_x = (mouse_position[0]-133) - (mouse_position[0]-133)%37 + 133
                        ylakulma_y = (mouse_position[1]-133) - (mouse_position[1]-133)%37 + 133
                        if board.board[int((ylakulma_y - 133)/37)][int((ylakulma_x - 133)/37)] == 0:
                            all_sprites.add(Miss(ylakulma_x, ylakulma_y))
                        else:
                            all_sprites.add(Hit(ylakulma_x, ylakulma_y))
                    else:
                        print("Et osunut kentälle")
        break_time = time.time() - start
        pygame.display.update()
        all_sprites.draw(screen)
        if break_time >= abort_time:
            break
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
