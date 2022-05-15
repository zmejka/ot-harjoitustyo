''' UI class for Scores of the Game.
    Arguments:
        background : color settings
        text_color : color settings for texts
        rect_color : color settings for objects

'''
import pygame

background = (151,210,203)
text_color = (0,51,102)
rect_color = (155, 255, 229)

class Scores:
    ''' Main menu for Scores of the game
        Arguments:
        screen : screen object
        width : screen width in pixels
        hight : screen hight in pixels
        '''
    def __init__(self, screen, width, hight):
        self.screen = screen
        self.title_font = pygame.font.SysFont('alias', 70)
        self.font = pygame.font.SysFont('alias', 40)
        self.w_mid = width/2
        self.h_mid = hight/2

    def scores(self, results):
        ''' Main menu screen and Scores subjects. '''
        title = self.title_font.render('Laivanupotus', True, text_color)
        scores = self.title_font.render('Tulokset', True, text_color)
        quit = self.font.render('Palaa Menu-valikkoon', True, text_color)

        if results[0][1] == 9999 or results == None:
            score1 = self.font.render('1. Tyhjä', True, text_color)
            score2 = self.font.render('2. Tyhjä', True, text_color)
            score3 = self.font.render('3. Tyhjä', True, text_color)
        elif len(results) == 3:
            score1 = self.font.render((f"1. {results[0][0]} on käyttänyt vain {results[0][1]} ammusta"), True, text_color)
            score2 = self.font.render((f"2. {results[1][0]} on käyttänyt vain {results[1][1]} ammusta"), True, text_color)
            score3 = self.font.render((f"3. {results[2][0]} on käyttänyt vain {results[2][1]} ammusta"), True, text_color)
        elif len(results) == 2:
            score1 = self.font.render((f"1. {results[0][0]} on käyttänyt vain {results[0][1]} ammusta"), True, text_color)
            score2 = self.font.render((f"2. {results[1][0]} on käyttänyt vain {results[1][1]} ammusta"), True, text_color)
            score3 = self.font.render('3. Tyhjä', True, text_color)
        else:
            score1 = self.font.render((f"1. {results[0][0]} on käyttänyt vain {results[0][1]} ammusta"), True, text_color)
            score2 = self.font.render('2. Tyhjä', True, text_color)
            score3 = self.font.render('3. Tyhjä', True, text_color)

        '''Texts on screen'''
        title_place = title.get_rect(center=(self.w_mid, self.h_mid/6))
        scores_place = scores.get_rect(center=(self.w_mid, (self.h_mid/2)))
        quit_place = quit.get_rect(center=(self.w_mid, (self.h_mid+300)))
        score1_place = score1.get_rect(center=(self.w_mid, self.h_mid-100))
        score2_place = score2.get_rect(center=(self.w_mid, self.h_mid))
        score3_place = score3.get_rect(center=(self.w_mid, self.h_mid+100))

        '''Main menu loop for returning to Main Menu'''
        running = True

        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.w_mid - 225 < mouse_pos[0] < self.w_mid + 225 and self.h_mid + 260 < mouse_pos[1] < self.h_mid + 330:
                        return

            self.screen.fill(background)

            if self.w_mid - 225 <= mouse_pos[0] <= self.w_mid + 225 and self.h_mid+ 250 <= mouse_pos[1] <= self.h_mid + 330:
                pygame.draw.rect(self.screen, rect_color, [self.w_mid-225, self.h_mid+260, 450, 70])

            self.screen.blit(title, title_place)
            self.screen.blit(scores, scores_place)
            self.screen.blit(quit, quit_place)
            self.screen.blit(score1, score1_place)
            self.screen.blit(score2, score2_place)
            self.screen.blit(score3, score3_place)
            pygame.display.update()
