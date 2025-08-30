import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_TEXT_WHITE, WIN_HEIGHT, EVENT_PLANETS, EVENT_OBSTACLES, COLOR_TEXT_GREEN, \
    FONT_JEDI, COLOR_TEXT_GREENYELLOW, EVENT_HEAL
from database.DBProxy import DBProxy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.speed_obstacles_max_value = 4
        self.keys_to_leave = [pygame.K_ESCAPE, pygame.K_BACKSPACE]

        # Database
        self.db = DBProxy('highscore')

        #score
        self.score = 0 # current score
        self.highscore = self.db.get_score()

        # Create Entities list
        self.bg_entity_list: list[Entity] = []
        self.md_entity_list: list[Entity] = []
        self.foreground_list: list[Entity] = [] # for effects (future implementation)

        ## Background
        self.bg_entity_list.extend(EntityFactory.get_entity('Starfield')) # Background
        pygame.time.set_timer(EVENT_PLANETS, 4000) # Background planets

        ## Players
        self.players = {'player1': EntityFactory.get_entity('Player1')}
        self.md_entity_list.append(self.players['player1'])
        if game_mode == '2P':
            self.players['player2'] = EntityFactory.get_entity('Player2')
            self.md_entity_list.append(self.players['player2'])

        ## Obstacles
        pygame.time.set_timer(EVENT_OBSTACLES, 3800) # Background planets

        ## Obstacles
        pygame.time.set_timer(EVENT_HEAL, 8500)


    def run(self):
        pygame.mixer_music.load(f'./assets/sounds/theme-song.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        is_running = True;
        while is_running:
            clock.tick(60)

            # Render Entities
            # 1st Background entities
            for ent in self.bg_entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # 2nd Midground entities
            for ent in self.md_entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    if ent.name == 'Player1':
                        self.players['player1'] = ent
                    elif ent.name == 'Player2':
                        self.players['player2'] = ent


            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    sys.exit()  # End pygame

                if event.type == pygame.KEYDOWN:
                    if event.key in self.keys_to_leave:
                        is_running = False

                ## Add planets for background
                if event.type == EVENT_PLANETS:
                    self.bg_entity_list.append(EntityFactory.get_entity('Planet'))

                # Add obstacles
                if event.type == EVENT_OBSTACLES:
                    self.md_entity_list.append(EntityFactory.get_entity('Obstacle', self.speed_obstacles_max_value))

                # Add Heal
                if event.type == EVENT_HEAL:
                    self.md_entity_list.append(EntityFactory.get_entity('Cure'))

            # HUD
            self.level_text(14, f'{self.name} - Score: {self.score}', COLOR_TEXT_WHITE, (10, 5))
            pos_y_health = 25
            i = 0
            for player in self.players.values():
                i = i +1
                self.level_text(16, f'HEALTH P{i}: {player.get_health()}', COLOR_TEXT_GREENYELLOW if i == 2 else COLOR_TEXT_GREEN, (10, pos_y_health))
                pos_y_health += 20

            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_TEXT_WHITE, (10, WIN_HEIGHT - 65))
            self.level_text(14, f'md Entities: {len(self.md_entity_list)}', COLOR_TEXT_WHITE, (10, WIN_HEIGHT - 45))
            self.level_text(14, f'md Bg ent: {len(self.bg_entity_list)}', COLOR_TEXT_WHITE, (10, WIN_HEIGHT - 25))
            pygame.display.flip()

            # Collision
            EntityMediator.verify_window_overflow(entity_list=self.md_entity_list)
            EntityMediator.verify_collision(entity_list=self.md_entity_list)
            EntityMediator.verify_health(entity_list=self.md_entity_list)

            # Verify game over
            if EntityMediator.game_over(self.players):
                if self.game_mode != '2P' and self.score > self.highscore:
                    self.db.update_or_create_score(self.score)
                is_running = False

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
