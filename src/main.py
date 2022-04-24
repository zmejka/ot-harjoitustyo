import pygame
from board import Board
from ui.menu import Menu
from ui.single import Single

CELL = 37
WIDTH = 37
HEIGHT = 20
FPS = 50

def main():
    screen_height = HEIGHT*CELL
    screen_width = WIDTH*CELL
    #game_field_left = Field(LEFTTOP-CELL-2, LEFTTOP-CELL-2)
    #game_field_right = Field(800,LEFTTOP-CELL-2)

    #board.print_board()

    # Initialize game window
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BattleShip")
    menu = Menu(screen, screen_width, screen_height)

    # Initialize sprites
    all_sprites = pygame.sprite.Group()
    #all_sprites.add(game_field_left)
    #all_sprites.add(game_field_right)
    #all_sprites.draw(screen)
    '''for j in board.ships:
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
                all_sprites.add(Destroyer(y_axis, x_axis))'''

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

            if menu.menu() == "Quit":
                pygame.sys.exit()

        pygame.display.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.sys.exit()

if __name__ == "__main__":
    main()
