from code.Background import Background
from code.Entity import Entity


class Planet(Entity):

    def __init__(self, name: str, position: tuple, speed: int, distance: int):
        super().__init__(name, position, speed)
        self.distance = distance

    def move(self, two_players: bool = False):
        self.rect.centerx -= self.__get_speed_based_on_distance()

    def __get_speed_based_on_distance(self) -> int:
        match self.distance:
            case 1:
                return 4
            case 2:
                return 3
            case 3:
                return 2
            case 4:
                return 1
        return 1