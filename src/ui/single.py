import pygame
from sprites.field import Field
from sprites.hit import Hit
from sprites.miss import Miss

background = (151,210,203)
CELL = 37
LTOP = 200
RTOP = LTOP + CELL*10

class Single:
    '''UI for single game
        Arguments:
        screen : screen object
        width : width of the screen in pixels
        hight : hight of the screen in pixels
        board : board object
        title_font : font settings
        '''
    def __init__(self, screen, width, hight, board):
        self.screen = screen
        self.width = width
        self.higth = hight
        self.board = board
        self.title_font = pygame.font.SysFont('alias', 70)
        self.font = pygame.font.SysFont('alias', 40)
        self.game = True

    def single_game(self):
        ''' Initializing of the game. '''
        self.screen.fill(background)
        title = self.title_font.render('Laivanupotus', True, (0,51,102))
        title_place = title.get_rect(center=(self.width/2, self.higth/12))
        cfield_title = self.font.render('Vastustajan kenttä', True, (0,51,102))
        cfield_place = cfield_title.get_rect(center=(LTOP+165, self.higth/5))
        game_field = Field(LTOP-CELL, LTOP-CELL)
        all_sprites = pygame.sprite.Group()
        pygame.display.update()
        all_sprites.add(game_field)
        all_sprites.draw(self.screen)
        self.screen.blit(title, title_place)
        self.screen.blit(cfield_title, cfield_place)

        '''Game loop '''
        clock = pygame.time.Clock()
        clock.tick(60)        
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_function = pygame.mouse.get_pressed()
                    mouse_position = pygame.mouse.get_pos()
                    if mouse_function[0]:
                        if game_field.rect.collidepoint(mouse_position):
                            self.mouse_event(mouse_position, all_sprites)
            pygame.display.update()
            all_sprites.draw(self.screen)

    def mouse_event(self, mouse_position, all_sprites):
        if mouse_position[0] <= LTOP or mouse_position[1] <= LTOP:
            return
        if mouse_position[0] >= RTOP or mouse_position[1] >= RTOP:
            return
        corner_x = (mouse_position[0]-LTOP) - (mouse_position[0]-LTOP)%CELL + LTOP
        corner_y = (mouse_position[1]-LTOP) - (mouse_position[1]-LTOP)%CELL + LTOP
        if self.board.board[int((corner_y-LTOP)/CELL)][int((corner_x - LTOP)/CELL)]==0:
            if self.board.shot(int((corner_y-LTOP)/CELL),int((corner_x - LTOP)/CELL)):
                all_sprites.add(Miss(corner_x, corner_y))
            else:
                print("ammukset loppui")
        elif self.board.board[int((corner_y-LTOP)/CELL)][int((corner_x - LTOP)/CELL)]==1:
            if self.board.shot(int((corner_y-LTOP)/CELL),int((corner_x - LTOP)/CELL)):
                all_sprites.add(Hit(corner_x, corner_y))
                if self.board.game_over():
                    print("peli loppui")
                    self.game = False

            else:
                print("ammukset loppui")
        else:
            print("Tähän kenttään on jo ammuttu!")
