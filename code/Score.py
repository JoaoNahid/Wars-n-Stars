import sys

import pygame

from code.Const import COLOR_TEXT_YELLOW, FONT_JEDI, WIN_WIDTH, WIN_HEIGHT
from code.MenuScreen import MenuScreen
from services.HighScoreService import HighScoreService


class Score(MenuScreen):
    def __init__(self, window):
        super().__init__(window)
        self.surf = pygame.image.load('./assets/images/Starfield.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.keys_to_leave = [pygame.K_ESCAPE, pygame.K_BACKSPACE, pygame.K_SPACE, pygame.K_RETURN]

        self.score = HighScoreService().get_score()

    def run(self):
        run_score = True
        while run_score:
            self.window.blit(source=self.surf, dest=self.rect)
            text_surf = self.mount_text(40, f'High Score: {self.score.score} ly', COLOR_TEXT_YELLOW, FONT_JEDI)
            position = text_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
            self.window.blit(source=text_surf, dest=position)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key in self.keys_to_leave:
                        run_score = False

            pygame.display.flip()
