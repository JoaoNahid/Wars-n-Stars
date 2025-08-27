import random

from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE
from code.Entity import Entity


class Obstacle(Entity):

    def __init__(self, name: str, file_path: str, position: tuple = (0,0), speed: int = 1):
        super().__init__(name, file_path, position, speed)
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    def move(self, two_players: bool = False):
        self.rect.centerx -= random.randint(1,4)
        pass