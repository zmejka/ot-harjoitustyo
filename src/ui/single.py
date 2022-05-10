''' UI class for Single Game.
    Arguments:
        background : color settings
        text_color : color settings
        CELL : edge of cell in pixels
        LTOP : constant for left corner x coordinate
        RTOP : constant for right corner x coordinate
'''

import pygame
from sprites.field import Field
from sprites.hit import Hit
from sprites.miss import Miss

background = (151,210,203)
text_color = (0,51,102)
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
        title_font : font settings for title
        font : font settings for other text
        game : game status. True, if game continue
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
        ''' Initializing of the game. 
            Set screen and background. Initialize sprite-list.
            Create game field. 
        '''
        self.screen.fill(background)
        title = self.title_font.render('Laivanupotus', True, text_color)
        title_place = title.get_rect(center=(self.width/2, self.higth/12))
        field_title = self.font.render('Vastustajan kenttä', True, text_color)
        field_place = field_title.get_rect(center=(LTOP+165, self.higth/5))
        ammo_text = self.font.render('Ammuksia jäljellä:', True, text_color)
        ammo_place = ammo_text.get_rect(center=(self.width/2+150, self.higth/3))
        ammo_start = self.title_font.render(str(self.board.get_ammo()), True, text_color)
        ammo_start_place = ammo_start.get_rect(center=(self.width/2+330, self.higth/3-10))
        game_field = Field(LTOP-CELL, LTOP-CELL)
        all_sprites = pygame.sprite.Group()
        pygame.display.update()
        all_sprites.add(game_field)
        all_sprites.draw(self.screen)
        self.screen.blit(title, title_place)
        self.screen.blit(field_title, field_place)
        self.screen.blit(ammo_text, ammo_place)
        self.screen.blit(ammo_start, ammo_start_place)

        ''' Game loop.
            Game continue until ammunition end or player sink all ships.
            On mouse left button click, shot on the board and check game status.
        '''
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
        ''' Functionality after pressing the left mouse button.
            Args:
                mouse_position : pair of coordinates
                all_sprites : list of sprites
        '''
        if mouse_position[0] <= LTOP or mouse_position[1] <= LTOP:
            return
        if mouse_position[0] >= RTOP or mouse_position[1] >= RTOP:
            return
        corner_x = (mouse_position[0]-LTOP) - (mouse_position[0]-LTOP)%CELL + LTOP
        corner_y = (mouse_position[1]-LTOP) - (mouse_position[1]-LTOP)%CELL + LTOP
        if self.board.board[int((corner_y-LTOP)/CELL)][int((corner_x - LTOP)/CELL)]==0:
            if self.board.shot(int((corner_y-LTOP)/CELL),int((corner_x - LTOP)/CELL)):
                all_sprites.add(Miss(corner_x, corner_y))
                self.ammo_counter()
            else:
                announcement = 'Peli on päättynyt! Ammukset loppuivat!'
                self.announcement(announcement)
                pygame.display.update()
                pygame.time.delay(500)
                self.game = False
        elif self.board.board[int((corner_y-LTOP)/CELL)][int((corner_x - LTOP)/CELL)]==1:
            if self.board.shot(int((corner_y-LTOP)/CELL),int((corner_x - LTOP)/CELL)):
                all_sprites.add(Hit(corner_x, corner_y))
                self.ammo_counter()
                if self.board.game_over():
                    announcement = 'Kaikki laivat on upotettu! Peli on päättynyt!'
                    self.announcement(announcement)
            else:
                announcement = 'Peli on päättynyt! Ammukset loppuivat!'
                self.announcement(announcement)
                pygame.display.update()
                pygame.time.delay(500)
                self.game = False
        else:
            announcement = 'Tähän kenttään on jo ammuttu!'
            self.announcement(announcement)

    def announcement(self, text):
        ''' Print a notification message at the bottom of the screen. 
        The message disappears after 1 second.    
        '''
        announcement = self.title_font.render(text, True, text_color)
        announcement_place = announcement.get_rect(center=(self.width/2, self.higth-100))
        self.screen.blit(announcement, announcement_place)
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.draw.rect(self.screen, background, [self.width/8, self.higth-200, 1000, 150])
        pygame.display.update()
    
    def ammo_counter(self):
        ''' Display the number of ammunition. The number is updated after each shot. '''
        pygame.draw.rect(self.screen, background, [self.width/2+300, self.higth/3-30, 60, 40])
        pygame.display.update()
        ammo = self.title_font.render(str(self.board.get_ammo()), True, text_color)
        place = ammo.get_rect(center=(self.width/2+330, self.higth/3-10))
        self.screen.blit(ammo, place)
            