import pygame.key

from pathlib import Path
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, ENTITY_HEALTH, ENTITY_DAMAGE
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, file_path: str, position: tuple = (0,0), speed: int = 1, keyboard: int = 1):
        super().__init__(name, file_path, position, speed)
        self.keyboard = keyboard
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.death_sound = pygame.mixer.Sound("./assets/sounds/explosion.wav")
        self.death_sound.set_volume(1)

    def update(self, ):
        pass

    def move(self, two_players: bool = False):
        pressed_key = pygame.key.get_pressed()
        key_up = pygame.K_w if self.keyboard == 1 else pygame.K_UP
        key_down = pygame.K_s if self.keyboard == 1 else pygame.K_DOWN
        if pressed_key[key_up] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.get_name()]
        if pressed_key[key_down] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.get_name()]

        key_left = pygame.K_a if self.keyboard == 1 else pygame.K_LEFT
        key_right = pygame.K_d if self.keyboard == 1 else pygame.K_RIGHT
        if pressed_key[key_left] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.get_name()]
        if pressed_key[key_right] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.get_name()]

    def get_name(self):
        return Path(self.name).stem

    def get_health(self):
        return self.health

    def reset_life(self):
        self.health = ENTITY_HEALTH[self.name]

    def die(self):
        channel = pygame.mixer.Channel(2)
        channel.play(self.death_sound)