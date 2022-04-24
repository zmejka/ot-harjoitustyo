import time
import pygame
from sprites.field import Field
from sprites.hit import Hit
from sprites.miss import Miss

background = (151,210,203)
CELL = 37
LEFTTOP = 160
LEFTBOTTOM = LEFTTOP + CELL*10

class Single:
    '''UI for single game
        Arguments:
        '''
    def __init__(self, screen, width, hight, board):
        self.screen = screen
        self.width = width
        self.higth = hight
        self.board = board
        self.title_font = pygame.font.SysFont('alias', 70)

    def single_game(self):
        self.screen.fill(background)
        title = self.title_font.render('Laivanupotus', True, (0,51,102))
        title_place = title.get_rect(center=(self.width/2, self.higth/12))
        game_field = Field(LEFTTOP-CELL, LEFTTOP-CELL)
        all_sprites = pygame.sprite.Group()
        pygame.display.update()
        all_sprites.add(game_field)
        all_sprites.draw(self.screen)
        self.screen.blit(title, title_place)

        single_game = True

        while single_game:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    single_game = False

                if i.type == pygame.MOUSEBUTTONDOWN:
                    mouse_function = pygame.mouse.get_pressed()
                    mouse_position = pygame.mouse.get_pos()
                    if mouse_function[0]:
                        if game_field.rect.collidepoint(mouse_position):
                            if mouse_position[0] <= LEFTTOP or mouse_position[1] <= LEFTTOP:
                                continue
                            if mouse_position[0] >= LEFTBOTTOM or mouse_position[1] >= LEFTBOTTOM:
                                continue
                            corner_x = (mouse_position[0]-LEFTTOP) - (mouse_position[0]-LEFTTOP)%CELL + LEFTTOP
                            corner_y = (mouse_position[1]-LEFTTOP) - (mouse_position[1]-LEFTTOP)%CELL + LEFTTOP
                            if self.board.board[int((corner_y-LEFTTOP)/CELL)][int((corner_x - LEFTTOP)/CELL)]==0:
                                if self.board.shot(int((corner_y-LEFTTOP)/CELL),int((corner_x - LEFTTOP)/CELL)):
                                    all_sprites.add(Miss(corner_x, corner_y))
                                else:
                                    print("ammukset loppui")
                            elif self.board.board[int((corner_y-LEFTTOP)/CELL)][int((corner_x - LEFTTOP)/CELL)]==1:
                                if self.board.shot(int((corner_y-LEFTTOP)/CELL),int((corner_x - LEFTTOP)/CELL)):
                                    all_sprites.add(Hit(corner_x, corner_y))
                                    self.board.game_over()
                                else:
                                    print("ammukset loppui")
                            else:
                                print("Tähän kenttään on jo ammuttu!")

                pygame.display.update()
                
                all_sprites.draw(self.screen)
