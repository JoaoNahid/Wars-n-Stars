import pygame

from code.Const import WIN_WIDTH, ENTITY_HEALTH
from code.Cure import Cure
from code.Obstacle import Obstacle
from code.Entity import Entity
from code.Planet import Planet
from code.Player import Player


class EntityMediator:

    @staticmethod
    def apply_damage(ent: Entity, damage: int):
        ent.health -= damage
        if ent.health < 0:
            ent.health = 0

    @staticmethod
    def heal_player(player, cure):
        percentage = cure.total_healing / 100
        if cure.total_healing == 9:
            player.health += ENTITY_HEALTH[player.name] * percentage
            if player.health > ENTITY_HEALTH[player.name]:
                player.health = ENTITY_HEALTH[player.name]
        else:
            new_cure = ENTITY_HEALTH[player.name] * percentage
            if player.health < new_cure:
                player.health = ENTITY_HEALTH[player.name] * percentage

        cure.health = 0

    @staticmethod
    def verify_window_overflow(entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, (Obstacle, Cure, Planet)) and ent.rect.right < 0:
                entity_list.remove(ent)

    @staticmethod
    def __verify_collision_between_entities(ent1, ent2):
        if (isinstance(ent1, Obstacle) and isinstance(ent2, Player)) or (isinstance(ent1, Player) and isinstance(ent2, Obstacle)):
            if pygame.Rect.colliderect(ent1.rect, ent2.rect):
                EntityMediator.apply_damage(ent1, ent2.damage)
                EntityMediator.apply_damage(ent2, ent1.damage)
        if isinstance(ent1, Cure) and isinstance(ent2, Player):
            if pygame.Rect.colliderect(ent1.rect, ent2.rect):
                EntityMediator.heal_player(ent2, ent1)
        if isinstance(ent2, Cure) and isinstance(ent1, Player):
            if pygame.Rect.colliderect(ent1.rect, ent2.rect):
                EntityMediator.heal_player(ent1, ent2)




    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent = entity_list[i]
            for j in range(i+1, len(entity_list)): # i + 1 prevent duplicated verification
                ent_to_compare = entity_list[j]
                if ent != ent_to_compare:
                    EntityMediator.__verify_collision_between_entities(ent, ent_to_compare)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, (Player, Obstacle, Cure)) and ent.health <= 0:
                ent.die()
                entity_list.remove(ent)

    @staticmethod
    def add_speed(entity_list: list[Entity], increment: int = 1):
        for ent in entity_list:
                ent.speed += increment

    @staticmethod
    def game_over(players) -> bool:
        total_health = 0
        for player in players.values():
            total_health += player.get_health()
        return total_health == 0

