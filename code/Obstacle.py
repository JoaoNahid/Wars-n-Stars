import random

import pygame.mixer

from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE
from code.Entity import Entity


class Obstacle(Entity):

    def __init__(self, name: str, file_path: str, position: tuple = (0,0), speed: int = 1):
        super().__init__(name, file_path, position, speed)
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.speed = random.randint(speed - 3, speed)
        self.death_sound = pygame.mixer.Sound('./assets/sounds/rock-breaking.wav')
        self.death_sound.set_volume(0.1)

    def move(self, two_players: bool = False):
        self.rect.centerx -= self.speed
        pass

    def die(self):
        channel = pygame.mixer.Channel(3)
        channel.play(self.death_sound)