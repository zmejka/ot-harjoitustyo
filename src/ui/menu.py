import pygame

background = (151,210,203)

class Menu:
    ''' Main menu for BattleShip game
        Arguments:
        width = screen width in pixels
        hight = screen hight in pixels '''
    def __init__(self, screen, width, hight):
        self.screen = screen
        self.title_font = pygame.font.SysFont('alias', 70)
        self.font = pygame.font.SysFont('alias', 50)
        self.w_mid = width/2
        self.h_mid = hight/2

    def menu(self):
        ''' Main menu screen and Menu subjects. '''
        title = self.title_font.render('Laivanupotus', True, (0,51,102))
        single = self.font.render('Yksinpeli', True, (0,51,102))
        player_vs_comp = self.font.render('Pelaaja vs Tietokone', True, (0,51,102))
        scores = self.font.render('Tulokset', True, (0,51,102))
        quit = self.font.render('Lopeta peli', True, (0,51,102))

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
                    if self.w_mid - 150 < mouse_pos[0] < self.w_mid + 150 and self.h_mid/4 + 160 < mouse_pos[1] < self.h_mid/4+230:
                        return "Single"

                    if self.w_mid - 150 < mouse_pos[0] < self.w_mid + 250 and self.h_mid/4 + 160 < mouse_pos[1] < self.h_mid/4+335:
                        return "PvC"

                    if self.w_mid - 150 < mouse_pos[0] < self.w_mid + 350 and self.h_mid/4 + 160 < mouse_pos[1] < self.h_mid/4+435:
                        return "Scores"

                    if self.w_mid - 150 < mouse_pos[0] < self.w_mid + 450 and self.h_mid/4 + 160 < mouse_pos[1] < self.h_mid/4+535:
                        return "Quit"


            self.screen.fill(background)

            if self.w_mid - 220 <= mouse_pos[0] <= self.w_mid + 220 and self.h_mid/4+140 <= mouse_pos[1] <= self.h_mid/4+225:
                pygame.draw.rect(self.screen, (155, 255, 229), [self.w_mid-200, self.h_mid/4+165, 400, 60])
            if self.w_mid - 220 <= mouse_pos[0] <= self.w_mid + 220 and self.h_mid/4+240 <= mouse_pos[1] <= self.h_mid/4+330:
                pygame.draw.rect(self.screen, (155, 255, 229), [self.w_mid-200, self.h_mid/4+265, 400, 60])
            if self.w_mid - 220 <= mouse_pos[0] <= self.w_mid + 220 and self.h_mid/4+340 <= mouse_pos[1] <= self.h_mid/4+430:
                pygame.draw.rect(self.screen, (160, 160, 160), [self.w_mid-200, self.h_mid/4+365, 400, 60])
            if self.w_mid - 220 <= mouse_pos[0] <= self.w_mid + 220 and self.h_mid/4+440 <= mouse_pos[1] <= self.h_mid/4+530:
                pygame.draw.rect(self.screen, (155, 255, 229), [self.w_mid-200, self.h_mid/4+465, 400, 60])

            self.screen.blit(title, title_place)
            self.screen.blit(single, single_place)
            self.screen.blit(player_vs_comp, player_vs_comp_place)
            self.screen.blit(scores, scores_place)
            self.screen.blit(quit, quit_place)
            pygame.display.update()
