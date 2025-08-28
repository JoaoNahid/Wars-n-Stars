from abc import ABC, abstractmethod
from locale import windows_locale

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import FONT_JEDI


class MenuScreen(ABC):

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/Starfield.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    @abstractmethod
    def run(self):
        pass

    def mount_text(self, font_size: int, text: str, text_color: tuple, font_family: str):
        font: Font = pygame.font.SysFont(name=font_family, size=font_size)
        text_surf: Surface = font.render(text, True, text_color).convert_alpha()
        return text_surf