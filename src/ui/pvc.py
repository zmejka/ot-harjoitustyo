import pygame
from sprites.field import Field
from sprites.hit import Hit
from sprites.miss import Miss
from sprites.carrier import Carrier
from sprites.carrier_vert import CarrierVert
from sprites.battleship import Battleship
from sprites.battleship_vert import BattleshipVert
from sprites.cruiser import Cruiser
from sprites.cruiser_vert import CruiserVert
from sprites.submarine import Submarine
from sprites.submarine_vert import SubmarineVert
from sprites.destroyer import Destroyer
from sprites.destroyer_vert import DestroyerVert

background = (151,210,203)
CELL = 37
LEFTTOP = 160
LEFTBOTTOM = LEFTTOP + CELL*10

class PvC:
    '''UI for player vs computer game
        Arguments:
        '''
    def __init__(self, screen, width, hight, board):
        self.screen = screen
        self.width = width
        self.higth = hight
        self.board = board
        self.title_font = pygame.font.SysFont('alias', 70)

    def pvc_game(self):
        self.screen.fill(background)
        title = self.title_font.render('Laivanupotus', True, (0,51,102))
        title_place = title.get_rect(center=(self.width/2, self.higth/12))
        field_player = Field(LEFTTOP-CELL, LEFTTOP-CELL)
        field_comp = Field(800,LEFTTOP-CELL)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(field_player)
        all_sprites.add(field_comp)

        for j in self.board.ships:
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

        pygame.display.update()

        all_sprites.draw(self.screen)
        self.screen.blit(title, title_place)

        pvc_game = True

        while pvc_game:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pvc_game = False

                if i.type == pygame.MOUSEBUTTONDOWN:
                    mouse_function = pygame.mouse.get_pressed()
                    mouse_position = pygame.mouse.get_pos()
                    if mouse_function[0]:
                        if field_player.rect.collidepoint(mouse_position):
                            if mouse_position[0] <= LEFTTOP or mouse_position[1] <= LEFTTOP:
                                continue
                            if mouse_position[0] >= LEFTBOTTOM or mouse_position[1] >= LEFTBOTTOM:
                                continue
                            corner_x = (mouse_position[0]-LEFTTOP) - (mouse_position[0]-LEFTTOP)%CELL + LEFTTOP
                            corner_y = (mouse_position[1]-LEFTTOP) - (mouse_position[1]-LEFTTOP)%CELL + LEFTTOP
                            if self.board.board[int((corner_y-LEFTTOP)/CELL)][int((corner_x - LEFTTOP)/CELL)]==0:
                                if self.board.shot(int((corner_y-LEFTTOP)/CELL),int((corner_x - LEFTTOP)/CELL)):
                                    all_sprites.add(Miss(corner_x, corner_y))
                            elif self.board.board[int((corner_y-LEFTTOP)/CELL)][int((corner_x - LEFTTOP)/CELL)]==1:
                                if self.board.shot(int((corner_y-LEFTTOP)/CELL),int((corner_x - LEFTTOP)/CELL)):
                                    all_sprites.add(Hit(corner_x, corner_y))
                                    self.board.game_over()

                pygame.display.update()
                
                all_sprites.draw(self.screen)
