import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_TEXT_WHITE, FONT_JEDI, \
    COLOR_TEXT_YELLOW, FONT_JEDI_BORDERED, FONT_JEDI_OUTLINE


class Menu:

    def __init__(self, window):
        self.window = window
        self.selected_option = 0
        self.surf = pygame.image.load('./assets/images/Starfield.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_options = ('New Game 1P', 'New Game 2P', 'Score', 'Tutorial', 'Exit' )

    def run(self) -> str:
        while True:
            # Draw Elements
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(65, "WARS'N", COLOR_TEXT_YELLOW, ((WIN_WIDTH / 2), 70), FONT_JEDI_OUTLINE)
            self.menu_text(65, "STARS", COLOR_TEXT_YELLOW, ((WIN_WIDTH / 2), 120), FONT_JEDI_OUTLINE)

            font_size = 15
            pos_y = 200
            for i in range(len(self.menu_options)):
                if i == self.selected_option:
                    self.menu_text(font_size, f'- {self.menu_options[i]}' , COLOR_TEXT_YELLOW, ((WIN_WIDTH / 2), pos_y), FONT_JEDI)
                else:
                    self.menu_text(font_size, self.menu_options[i], COLOR_TEXT_YELLOW, ((WIN_WIDTH / 2), pos_y), FONT_JEDI)

                #  calculate next pos_y
                font_size += 10
                pos_y += font_size * 1

            pygame.display.flip()

            # Check all events
            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option += 1
                        if self.selected_option == len(self.menu_options):
                            self.selected_option = 0

                    if event.key == pygame.K_UP:
                        self.selected_option -= 1
                        if self.selected_option < 0:
                            self.selected_option = len(self.menu_options) - 1

                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        return self.menu_options[self.selected_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font: str):
        text_font: Font = pygame.font.SysFont(name=font, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)