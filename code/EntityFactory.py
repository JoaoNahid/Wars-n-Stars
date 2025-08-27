import random

from code.Background import Background
from code.Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT
from code.Obstacle import Obstacle
from code.Planet import Planet
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Starfield':
                list_bg = [Background('Starfield', 'Starfield.jpg', (0, 0), ENTITY_SPEED['Starfield']),
                           Background('Starfield', 'Starfield.jpg', (WIN_WIDTH, 0), ENTITY_SPEED['Starfield'])]
                return list_bg
            case 'Planet':
                return Planet('Planet', f'Planet{random.randint(1,12)}.png', (WIN_WIDTH + 10, random.randint(-5, WIN_HEIGHT + 5)), 1, random.randint(1,3) )
            case 'Player1':
                return Player('Player1', 'Player1.png', (10, WIN_HEIGHT / 2), 1)
            case 'Player2':
                return Player('Player2', 'Player2', (10, WIN_HEIGHT * 0.75), 1, keyboard=2)
            case 'Obstacle':
                obstacle = EntityFactory.define_obstacle()
                path = f'asteroids/{obstacle["type"]}{random.randint(obstacle['range'][0], obstacle['range'][1])}.png'
                return Obstacle(obstacle["type"], path, (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 30)))

    @staticmethod
    def define_obstacle():
        possibilities = [
            {'type':'lg_asteroid', 'range': (1, 112)},
            {'type':'md_asteroid', 'range': (1, 160)},
            {'type':'sm_asteroid', 'range': (1, 96)},
        ]
        return random.choices(possibilities, [25, 35, 40], k=1)[0] # choice random with weights