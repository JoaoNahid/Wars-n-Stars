import random

import pygame

from code.Entity import Entity


class Planet(Entity):

    def __init__(self, name: str, position: tuple, speed: int, distance: int):
        super().__init__(name, position, speed)
        self.distance = distance
        self.surf = self.__apply_distance_effect()
        self.surf = self.__resize_planet_based_on_distance()

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

    def __apply_distance_effect(self):
        darkness_levels = {1: 0.0, 2: 0.3, 3: 0.6, 4: 0.8}
        darkness = darkness_levels.get(self.distance, 0.0)

        if darkness == 0:
            return self.surf

        result = self.surf.copy()
        pixel_array = pygame.PixelArray(result)

        for x in range(result.get_width()):
            for y in range(result.get_height()):
                color = result.get_at((x, y))
                if color[3] > 0:  # get non transparent fields
                    new_color = (
                        int(color[0] * (1 - darkness)),
                        int(color[1] * (1 - darkness)),
                        int(color[2] * (1 - darkness)),
                        color[3]
                    )
                    pixel_array[x, y] = new_color

        del pixel_array
        return result

    def __resize_planet_based_on_distance(self):
        base_size_factors = {1: 1.0, 2: 0.8, 3: 0.6, 4: 0.4}
        base_scale = base_size_factors.get(self.distance, 1.0)

        variation = random.uniform(0.8, 1.2)
        scale_factor = base_scale * variation

        original_width, original_height = self.surf.get_size()
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        new_width = max(10, new_width)
        new_height = max(10, new_height)

        return pygame.transform.smoothscale(self.surf, (new_width, new_height))
