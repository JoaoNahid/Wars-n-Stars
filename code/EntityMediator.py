import pygame

from code.Const import WIN_WIDTH
from code.Obstacle import Obstacle
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def apply_damage(ent: Entity, damage: int):
        ent.health -= damage

    @staticmethod
    def verify_window_overflow(entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, Obstacle) and ent.rect.right < 0:
                entity_list.remove(ent)

    @staticmethod
    def __verify_collision_between_entities(ent1, ent2):
        if (isinstance(ent1, Obstacle) and isinstance(ent2, Player)) or (isinstance(ent1, Player) and isinstance(ent2, Obstacle)):
            if pygame.Rect.colliderect(ent1.rect, ent2.rect):
                EntityMediator.apply_damage(ent1, ent2.damage)
                EntityMediator.apply_damage(ent2, ent1.damage)


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent = entity_list[i]
            EntityMediator.__verify_window_overflow(ent)
            for j in range(i+1, len(entity_list)): # i + 1 prevent duplicated verification
                ent_to_compare = entity_list[j]
                if ent != ent_to_compare:
                    EntityMediator.__verify_collision_between_entities(ent, ent_to_compare)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, (Player, Obstacle)) and ent.health <= 0:
                entity_list.remove(ent)

    @staticmethod
    def add_speed(entity_list: list[Entity]):
        for ent in entity_list:
            ent.speed += 1