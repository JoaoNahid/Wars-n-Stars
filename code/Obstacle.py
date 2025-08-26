import random

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Obstacle(Entity):

    def __init__(self, name: str, position: tuple = (0,0), speed: int = 1):
        super().__init__(name, position, speed)

    def move(self, two_players: bool = False):
        self.rect.centerx -= random.randint(1,4)
        pass