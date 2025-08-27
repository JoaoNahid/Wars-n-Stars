from abc import ABC, abstractmethod

import pygame


# ABC mean that is a abstract class
class Entity(ABC):

    def __init__(self, name: str, file_path: str, position: tuple, speed: int):
        self.name = name
        self.surf = pygame.image.load('./assets/images/' + file_path).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = speed

    @abstractmethod #decorator
    def move(self, two_players: bool = False):
        pass