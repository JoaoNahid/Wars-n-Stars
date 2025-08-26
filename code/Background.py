
from code.Const import WIN_WIDTH
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position, speed)

    def move(self, two_players: bool = False):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH