''' UI class for Main Menu of the Game.
    Arguments:
        background : color settings
        text_color : color settings for texts
        rect_color : color settings for objects
        
'''
import pygame

background = (151,210,203)
text_color = (0,51,102)
rect_color = (155, 255, 229)

class Menu:
    ''' Main menu for BattleShip game
        Arguments:
        screen : screen object
        width : screen width in pixels
        hight : screen hight in pixels
        font : font settings
        '''
    def __init__(self, screen, width, hight):
        self.screen = screen
        self.title_font = pygame.font.SysFont('alias', 70)
        self.font = pygame.font.SysFont('alias', 50)
        self.w_mid = width/2
        self.h_mid = hight/2

    def menu(self):
        ''' Main menu screen and Menu subjects. '''
        title = self.title_font.render('Laivanupotus', True, text_color)
        single = self.font.render('Yksinpeli', True, text_color)
        player_vs_comp = self.font.render('Pelaaja vs Tietokone', True, text_color)
        scores = self.font.render('Tulokset', True, text_color)
        quit = self.font.render('Lopeta peli', True, text_color)

        '''Text on screen'''
        title_place = title.get_rect(center=(self.w_mid, self.h_mid/6))
        single_place = single.get_rect(center=(self.w_mid, self.h_mid/4+200))
        player_vs_comp_place = player_vs_comp.get_rect(center=(self.w_mid, self.h_mid/4+300))
        scores_place = scores.get_rect(center=(self.w_mid, (self.h_mid/4+400)))
        quit_place = quit.get_rect(center=(self.w_mid, (self.h_mid/4+500)))

        '''Main menu loop'''
        menu = True

        while menu:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.w_mid - 200 < mouse_pos[0] < self.w_mid + 200 and self.h_mid/4 + 160 < mouse_pos[1] < self.h_mid/4+230:
                        return "Single"

                    if self.w_mid - 200 < mouse_pos[0] < self.w_mid + 200 and self.h_mid/4 + 260 < mouse_pos[1] < self.h_mid/4+330:
                        return "PvC"

                    if self.w_mid - 200 < mouse_pos[0] < self.w_mid + 200 and self.h_mid/4 + 360 < mouse_pos[1] < self.h_mid/4+430:
                        return "Scores"

                    if self.w_mid - 200 < mouse_pos[0] < self.w_mid + 200 and self.h_mid/4 + 460 < mouse_pos[1] < self.h_mid/4+530:
                        return "Quit"


            self.screen.fill(background)

            if self.w_mid - 200 <= mouse_pos[0] <= self.w_mid + 200 and self.h_mid/4+160 <= mouse_pos[1] <= self.h_mid/4+230:
                pygame.draw.rect(self.screen, rect_color, [self.w_mid-200, self.h_mid/4+160, 400, 70])
            if self.w_mid - 200 <= mouse_pos[0] <= self.w_mid + 200 and self.h_mid/4+260 <= mouse_pos[1] <= self.h_mid/4+330:
                pygame.draw.rect(self.screen, rect_color, [self.w_mid-200, self.h_mid/4+260, 400, 70])
            if self.w_mid - 200 <= mouse_pos[0] <= self.w_mid + 200 and self.h_mid/4+360 <= mouse_pos[1] <= self.h_mid/4+430:
                pygame.draw.rect(self.screen, rect_color, [self.w_mid-200, self.h_mid/4+360, 400, 70])
            if self.w_mid - 200 <= mouse_pos[0] <= self.w_mid + 200 and self.h_mid/4+460 <= mouse_pos[1] <= self.h_mid/4+530:
                pygame.draw.rect(self.screen, rect_color, [self.w_mid-200, self.h_mid/4+460, 400, 70])

            self.screen.blit(title, title_place)
            self.screen.blit(single, single_place)
            self.screen.blit(player_vs_comp, player_vs_comp_place)
            self.screen.blit(scores, scores_place)
            self.screen.blit(quit, quit_place)
            pygame.display.update()
