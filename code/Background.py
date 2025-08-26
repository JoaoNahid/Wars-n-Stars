import random

from code.Const import WIN_WIDTH
from code.Entity import Entity
from code.Planet import Planet


class Background(Entity):

    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position, speed)
        self.planets: list[Planet] = []
        self.last_planet_time = 0
        self.next_planet_interval = random.randint(1000, 5000)

    def move(self, two_players: bool = False):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH