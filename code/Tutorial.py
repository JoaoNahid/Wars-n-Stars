import sys

import pygame
from pygame import Surface

from code.Const import WIN_HEIGHT, COLOR_TEXT_YELLOW, WIN_WIDTH, FONT_JEDI, FONT_JEDI_OUTLINE, COLOR_TEXT_WHITE
from code.MenuScreen import MenuScreen


class Tutorial(MenuScreen):
    def __init__(self, window):
        super().__init__(window)
        self.surf = pygame.image.load('./assets/images/Starfield.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.window.blit(source=self.surf, dest=self.rect)
            # Text
            title = self.mount_text(20, 'tutorial', COLOR_TEXT_WHITE, FONT_JEDI_OUTLINE)
            title_pos = title.get_rect(center=(WIN_WIDTH / 2, 25))
            self.window.blit(source=title, dest=title_pos)

            font_size = 8
            pos_y = 60
            for i in range(len(self.__tutorial_text())):
                text_surf: Surface = self.mount_text(font_size, self.__tutorial_text()[i], COLOR_TEXT_YELLOW, FONT_JEDI)
                position = text_surf.get_rect(center=((WIN_WIDTH / 2), pos_y))
                self.window.blit(source=text_surf, dest=position)

                #  calculate next pos_y
                font_size += 1
                pos_y += font_size * 1

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

    def __tutorial_text(self) -> list:
        return [
            "piloto,  sua  nave  já  está pronta  para",
            "decolar. Use os controles W,  A,  S  e  D",
            "para manobrar em  meio  ao  vasto  e",
            "perigoso    campo     de     destroços.",
            "Mantenha-se  atento:  os  asteroides",
            "são  inúmeros  e  um  único   impacto",
            "poderá ser fatal.                        ",
            "",
            "Se encontrar pedaços de aeronaves",
            "flutuando, colete-os, eles servirão",
            "para   reparar   parte  dos  danos",
            "sofridos e manter  sua  nave  ativa.",
            "Seu objetivo é simples, mas ao mesmo",
            "tempo  vital:  voe  o  mais distante",
            "que  puder.                                 ",
            "",
            "que   a  força   esteja   com   você!"
        ]


