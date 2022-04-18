import time
import pygame
from board import Board
from sprites.field import Field
from sprites.hit import Hit
from sprites.miss import Miss
from sprites.submarine import Submarine
from sprites.submarine_vert import SubmarineVert
from sprites.carrier import Carrier
from sprites.carrier_vert import CarrierVert
from sprites.battleship import Battleship
from sprites.battleship_vert import BattleshipVert
from sprites.cruiser import Cruiser
from sprites.cruiser_vert import CruiserVert
from sprites.destroyer import Destroyer
from sprites.destroyer_vert import DestroyerVert


CELL = 37
WIDTH = 37
HEIGHT = 20
LEFTTOP = 150
LEFTBOTTOM = LEFTTOP + CELL*11
FPS = 50

def main():
    # Initialize board and ships
    board = Board()
    board.create_ships()
    board.randomize_ships()
    #game_board = GameBoard(board, CELL)
    screen_height = HEIGHT*CELL
    screen_width = WIDTH*CELL
    game_field_left = Field(LEFTTOP-CELL-2, LEFTTOP-CELL-2)
    game_field_right = Field(800,LEFTTOP-CELL-2)
    
    board.print_board()

    # Initialize game window
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BattleShip")

    background = (151,210,203)
    screen.fill(background)
    all_sprites = pygame.sprite.Group()
    pygame.display.update()

    # Initialize sprites
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(game_field_left)
    all_sprites.add(game_field_right)
    all_sprites.draw(screen)
    for j in board.ships:
        name = j.get_name()
        coordinates = j.position
        orientation = j.get_orientation()
        x_axis = LEFTTOP + coordinates[0]*CELL
        y_axis = LEFTTOP + coordinates[1]*CELL
        if orientation == 1:
            if name == "Submarine":
                all_sprites.add(SubmarineVert(y_axis, x_axis))
            elif name == "Carrier":
                all_sprites.add(CarrierVert(y_axis, x_axis))
            elif name == "Cruiser":
                all_sprites.add(CruiserVert(y_axis, x_axis))
            elif name == "Battleship":
                all_sprites.add(BattleshipVert(y_axis, x_axis))
            else:
                all_sprites.add(DestroyerVert(y_axis, x_axis))
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
                    if game_field_left.rect.collidepoint(mouse_position):
                        if mouse_position[0] < LEFTTOP or mouse_position[1] < LEFTTOP:
                            continue
                        if mouse_position[0] > LEFTBOTTOM or mouse_position[1] > LEFTBOTTOM:
                            continue
                        corner_x = (mouse_position[0]-LEFTTOP) - (mouse_position[0]-LEFTTOP)%CELL + LEFTTOP
                        corner_y = (mouse_position[1]-LEFTTOP) - (mouse_position[1]-LEFTTOP)%CELL + LEFTTOP
                        if board.board[int((corner_y-LEFTTOP)/CELL)][int((corner_x - LEFTTOP)/CELL)]==0:
                            all_sprites.add(Miss(corner_x, corner_y))
                            board.shot(int((corner_y-LEFTTOP)/CELL),int((corner_x - LEFTTOP)/CELL))
                        elif board.board[int((corner_y-LEFTTOP)/CELL)][int((corner_x - LEFTTOP)/CELL)]==1:
                            all_sprites.add(Hit(corner_x, corner_y))
                            board.shot(int((corner_y-LEFTTOP)/CELL),int((corner_x - LEFTTOP)/CELL))
                            board.game_over()
                        else:
                            print("Tähän kenttään on jo ammuttu!")
                    else:
                        print("Et osunut kentälle")
        break_time = time.time() - start
        pygame.display.update()
        all_sprites.draw(screen)
        if break_time >= abort_time:
            board.print_board()
            break
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
