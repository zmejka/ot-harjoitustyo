''' UI class for Player vs Computer Game.
    Arguments:
        background : color settings
        text_color : color settings
        CELL : edge of cell in pixels
        LTOP : constant for left corner x coordinate
        RTOP : constant for right corner x coordinate
        FPS : frame per second
'''

import pygame
from results import Results
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
from objects.player import Player
from objects.ship import Ship

background = (151,210,203)
text_color = (0,51,102)
CELL = 37
LTOP = 200
RTOP = LTOP+CELL*10+250
FPS = 60

class PvC:
    '''UI for player vs computer game
        Arguments:
        screen : screen object
        width : width of the screen in pixels
        hight : hight of the screen in pixels
        player_board : board object for player ships
        ai_board : board object for computer
        title_font & font : font settings
        player & computer : player-objects
        game : status of the game
        results_file : results object
        '''
    def __init__(self, screen, width, hight, player_board, ai_board):
        self.screen = screen
        self.width = width
        self.higth = hight
        self.player_board = player_board
        self.comp_board = ai_board
        self.title_font = pygame.font.SysFont('alias', 70)
        self.announcement_font = pygame.font.SysFont('alias', 40)
        self.font = pygame.font.SysFont('alias', 40)
        self.player = Player("Pelaaja PvC", True)
        self.computer = Player("AI", False)
        self.game = True
        self.result_file = Results()

    def initialize(self):
        ''' Initializing the game. '''
        self.screen.fill(background)
        title = self.title_font.render('Laivanupotus', True, (0,51,102))
        pfield_title = self.font.render('Oma kenttä', True, (0,51,102))
        cfield_title = self.font.render('Vastustajan kenttä', True, (0,51,102))
        title_place = title.get_rect(center=(self.width/2, self.higth/12))
        pfield_place = pfield_title.get_rect(center=(RTOP+165, self.higth/5))
        cfield_place = cfield_title.get_rect(center=(LTOP+165, self.higth/5))
        field_comp = Field(LTOP-CELL, LTOP-CELL)
        field_player = Field(RTOP-CELL,LTOP-CELL)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(field_player)
        all_sprites.add(field_comp)
        all_sprites.draw(self.screen)
        self.screen.blit(title, title_place)
        self.screen.blit(pfield_title, pfield_place)
        self.screen.blit(cfield_title, cfield_place)
        pygame.display.update()
        self.place_ships(field_player, all_sprites)
        self.pvc_game(all_sprites, field_comp)

    def place_ships(self, field_player, all_sprites):
        ''' Before starting player put 5 ships on right board. 
            Args:
                field_player : player's field object
                all_sprites : list of sprites
        '''
        ships = [('Lentotukialus', 5), ('Taistelulaiva',4), ('Risteilijä',3), ('Sukellusvene',3), ('Hävittäjä',2)]
        clock = pygame.time.Clock()
        clock.tick(FPS)
        announcement = 'Aseta laivat oikeapuoliselle kentälle! Vasen näppäin = vaaka, oikea näppäin = pysty.'
        self.announcement(announcement)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_func = pygame.mouse.get_pressed()
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_func[0]:
                        if field_player.rect.collidepoint(mouse_pos):
                            self.player_ship(mouse_pos, ships, all_sprites, mouse_func)
                    if mouse_func[2]:
                        if field_player.rect.collidepoint(mouse_pos):
                            self.player_ship(mouse_pos, ships, all_sprites, mouse_func)
                    all_sprites.draw(self.screen)
                pygame.display.flip()
                if not ships:
                    announcement = 'Kaikki pelaajan laivat on kentällä! Peli on alkanut!'
                    self.announcement(announcement)
                    running = False
    
    def pvc_game(self, all_sprites, field_comp):
        ''' Game loop 
            Args:
                field_comp : computer's field object
                all_sprites : list of sprites
        '''
        quit = self.font.render('Palaa', True, text_color)
        quit_place = quit.get_rect(center=(self.width-60, 40))
        self.screen.blit(quit, quit_place)
        clock = pygame.time.Clock()
        clock.tick(FPS)
        while self.game:
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if self.computer.get_status():
                    self.comp_event(all_sprites)
                    self.computer.set_status(False)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_function = pygame.mouse.get_pressed()
                    if self.width - 100 < mouse_position[0] < self.width-20 and 15 < mouse_position[1] < 65:
                        return
                    if mouse_function[0]:
                        if field_comp.rect.collidepoint(mouse_position):
                            self.player_event(mouse_position, all_sprites)
                            self.computer.set_status(True)
                            pygame.time.delay(50)
            if self.width - 100 <= mouse_position[0] <= self.width-20 and 15 <= mouse_position[1] <= 65:
                pygame.draw.rect(self.screen, (155, 255, 229), [self.width - 100, 15, 80, 50])
            self.screen.blit(quit, quit_place)
            all_sprites.draw(self.screen)
            pygame.display.flip()

    def player_event(self, mouse_position, all_sprites):
        ''' Player's shooting functionality.
            Args:
                mouse_position : 2 mouse position coordinates in pixels
                all_sprites : list of sprites
        '''
        if mouse_position[0] <= LTOP or mouse_position[1] <= LTOP:
            return
        if mouse_position[0] >= RTOP-250 or mouse_position[1] >= RTOP-250:
            return
        corner_x = (mouse_position[0]-LTOP) - (mouse_position[0]-LTOP)%CELL + LTOP
        corner_y = (mouse_position[1]-LTOP) - (mouse_position[1]-LTOP)%CELL + LTOP
        if self.comp_board.board[int((corner_y-LTOP)/CELL)][int((corner_x - LTOP)/CELL)]==0:
            if self.comp_board.shot(int((corner_y-LTOP)/CELL),int((corner_x - LTOP)/CELL)):
                all_sprites.add(Miss(corner_x, corner_y))
        elif self.comp_board.board[int((corner_y-LTOP)/CELL)][int((corner_x - LTOP)/CELL)]==1:
            if self.comp_board.shot(int((corner_y-LTOP)/CELL),int((corner_x - LTOP)/CELL)):
                all_sprites.add(Hit(corner_x, corner_y))
                if self.comp_board.notices:
                    self.sunken_ships_computer()
                if self.comp_board.game_over():
                    announcement = 'Kaikki vastustajan laivat on upotettu! Peli on päättynyt!'
                    self.announcement(announcement)
                    self.result_file.write_results((self.player.get_name(), 100-self.player_board.get_ammo()))
                    self.game = False
        else:
            announcement = 'Tähän kenttään on jo ammuttu!'
            self.announcement(announcement)

    def comp_event(self, all_sprites):
        ''' Computer's shooting functionality.
            Args:
                all_sprites : list of sprites
        '''
        coordinates = self.player_board.comp_shot()
        corner_x = coordinates[0]*CELL + LTOP
        corner_y = coordinates[1]*CELL + RTOP
        if self.player_board.board[coordinates[0]][coordinates[1]]==2:
            all_sprites.add(Miss(corner_y, corner_x))
        elif self.player_board.board[coordinates[0]][coordinates[1]]==3:
            all_sprites.add(Hit(corner_y, corner_x))
            if self.player_board.notices:
                self.sunken_ships_player()
            if self.player_board.game_over():
                announcement = 'Kaikki pelaajan laivat on upotettu! Peli on päättynyt!'
                self.announcement(announcement)
                self.game = False

    def player_ship(self, mouse_pos, ships, all_sprites, mouse_func):
        ''' Player's ship layout functionality.
            Args:
                mouse_pos : mouse position coordinates in pixels
                ships : list of the names of the ship's
                all_sprites : list of sprites
                mouse_func : list of the mouse get_pressed function :
                    0 - left button pressed, 2 - right button pressed
        '''
        if mouse_pos[0] <= RTOP or mouse_pos[1] <= LTOP:
            return
        x_axis = (mouse_pos[0]-RTOP) - (mouse_pos[0]-RTOP)%CELL + RTOP
        y_axis = (mouse_pos[1] -LTOP) - (mouse_pos[1]-LTOP)%CELL + LTOP
        row = int((mouse_pos[1]-LTOP)/CELL)
        col = int((mouse_pos[0]-RTOP)/CELL)
        coordinates = (row, col)
        name = ships[0][0]
        length = ships[0][1]
        if mouse_func[0]:
            orientation = 0
        if mouse_func[2]:
            orientation = 1
        ship = Ship(name, length, orientation)
        self.player_board.ships.append(ship)
        if self.player_board.place_the_ship(ship, coordinates, orientation, length):
            if orientation == 0:
                if name=='Lentotukialus':
                    all_sprites.add(Carrier(x_axis, y_axis))
                elif name=='Taistelulaiva':
                    all_sprites.add(Battleship(x_axis, y_axis))
                elif name=='Risteilijä':
                    all_sprites.add(Cruiser(x_axis, y_axis))
                elif name=='Sukellusvene':
                    all_sprites.add(Submarine(x_axis, y_axis))
                else:
                    all_sprites.add(Destroyer(x_axis, y_axis))
            if orientation == 1:
                if name=='Lentotukialus':
                    all_sprites.add(CarrierVert(x_axis, y_axis))
                elif name=='Taistelulaiva':
                    all_sprites.add(BattleshipVert(x_axis, y_axis))
                elif name=='Risteilijä':
                    all_sprites.add(CruiserVert(x_axis, y_axis))
                elif name=='Sukellusvene':
                    all_sprites.add(SubmarineVert(x_axis, y_axis))
                else:
                    all_sprites.add(DestroyerVert(x_axis, y_axis))    
            ships.pop(0)
            pygame.display.flip()

    def announcement(self, text):
        ''' Print a notification message at the bottom of the screen. 
            The message disappears after 1 second.    
        '''
        announcement = self.announcement_font.render(text, True, (0,51,102))
        announcement_place = announcement.get_rect(center=(self.width/2, self.higth-80))
        self.screen.blit(announcement, announcement_place)
        pygame.display.update()
        pygame.time.delay(1500)
        pygame.draw.rect(self.screen, background, [self.width/10-30, self.higth-120, 1200, 120])
        pygame.display.update()

    def sunken_ships_player(self):
        ''' Display list of player's sunken ships on right side of the screen. '''
        pygame.draw.rect(self.screen, background, [LTOP*4-20, LTOP*3-20, 400, 100])
        pygame.display.update()
        sunken_ships = self.font.render(str(self.player_board.notices[len(self.player_board.notices)-1]), True, text_color)
        place = sunken_ships.get_rect(center=(LTOP*4+180, LTOP*3))
        self.screen.blit(sunken_ships, place)

    def sunken_ships_computer(self):
        ''' Display list of computers's sunken ships on left side of the screen. '''
        pygame.draw.rect(self.screen, background, [LTOP-70, LTOP*3-20, 430, 100])
        pygame.display.update()
        sunken_ships = self.font.render(str(self.comp_board.notices[len(self.comp_board.notices)-1]), True, text_color)
        place = sunken_ships.get_rect(center=(LTOP+160, LTOP*3))
        self.screen.blit(sunken_ships, place)
