import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_TEXT_WHITE, WIN_HEIGHT, EVENT_PLANETS, WIN_WIDTH, EVENT_OBSTACLES, COLOR_TEXT_GREEN, \
    FONT_JEDI, COLOR_TEXT_GREENYELLOW
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.score = 0 #
        self.speed_obstacles_max_value = 4

        # Create Entities list
        self.bg_entity_list: list[Entity] = []
        self.md_entity_list: list[Entity] = []
        self.foreground_list: list[Entity] = [] # for effects (future implementation)

        ## Background
        self.bg_entity_list.extend(EntityFactory.get_entity('Starfield')) # Background
        pygame.time.set_timer(EVENT_PLANETS, 4000) # Background planets

        ## Players
        self.md_entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode == '2P':
            self.md_entity_list.append(EntityFactory.get_entity('Player2'))

        ## Obstacles
        pygame.time.set_timer(EVENT_OBSTACLES, 2000) # Background planets



    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            # Render Entities
            # 1st Background entities
            for ent in self.bg_entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move(self.game_mode == '2P')

            # 2nd Midground entities
            for ent in self.md_entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move(self.game_mode == '2P')
                if isinstance(ent, Player):
                    if ent.name == 'Player1':
                        self.level_text(16, f'HEALTH P1: {ent.get_health()}', COLOR_TEXT_GREEN, (10, 20))
                    elif ent.name == 'Player2':
                        self.level_text(16, f'HEALTH P2: {ent.get_health()}', COLOR_TEXT_GREENYELLOW, (10, 35))


            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    sys.exit()  # End pygame

                if event.type == EVENT_PLANETS:
                    self.bg_entity_list.append(EntityFactory.get_entity('Planet'))

                if event.type == EVENT_OBSTACLES:
                    self.md_entity_list.append(EntityFactory.get_entity('Obstacle', self.speed_obstacles_max_value))

            # print text
            self.level_text(14, f'{self.name} - Score: {self.score}', COLOR_TEXT_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_TEXT_WHITE, (10, WIN_HEIGHT - 25))
            pygame.display.flip()

            # Collision
            EntityMediator.verify_window_overflow(entity_list=self.md_entity_list)
            EntityMediator.verify_collision(entity_list=self.md_entity_list)
            EntityMediator.verify_health(entity_list=self.md_entity_list)

            # Score
            self.score += 1
            if self.score % 1000 == 0:
                self.speed_obstacles_max_value += 1
                EntityMediator.add_speed(entity_list=self.bg_entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name=FONT_JEDI, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
