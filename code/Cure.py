import pygame

from code.Entity import Entity


class Cure(Entity):
    def __init__(self, name, file_path, position, speed):
        super().__init__(name, file_path, position, speed)
        self.health = 50
        self.speed = speed

        self.death_sound = pygame.mixer.Sound("./assets/sounds/heal.wav")
        self.death_sound.set_volume(1)

    def move(self):
        self.rect.centerx -= self.speed

    def die(self):
        channel = pygame.mixer.Channel(2)
        channel.play(self.death_sound)