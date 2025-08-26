import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_TEXT_WHITE, WIN_HEIGHT, EVENT_PLANETS, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.timeout = 20000 # 20 segundos
        # Create Entities
        self.entity_list.extend(EntityFactory.get_entity('Starfield')) # Background
        pygame.time.set_timer(EVENT_PLANETS, 1000) # Background planets
        # self.entity_list.append(EntityFactory.get_entity('Player1'))
        # if game_mode == '2P':
        #     self.entity_list.append(EntityFactory.get_entity('Player2'))


    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move(self.game_mode == '2P')

            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    sys.exit()  # End pygame

                if event.type == EVENT_PLANETS:
                    self.entity_list.append(EntityFactory.get_entity('Planet', (WIN_WIDTH, random.randint(-15, WIN_HEIGHT + 10))))

            # print text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_TEXT_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_TEXT_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entities: {len(self.entity_list)}', COLOR_TEXT_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Degree timeout
            self.timeout -= 1

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Montserrat', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
