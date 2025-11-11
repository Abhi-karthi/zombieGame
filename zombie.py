import pygame
import random
import time
from build_animations import *


class Zombie:
    def __init__(self, level: int):
        self.level = level
        if random.randint(0, 2) == 0:
            self.x = -20
        else:
            self.x = 1940
        self.y = 0
        self.reset_time = time.time()
        self.reset_cooldown = 3
        self.attacking_animation = zombie_attack_animation
        self.walking_animation = zombie_walking_animation
        self.dead_animation = zombie_dead_animation
        # size of screen: 1920x1050

    def get_reset_time(self) -> bool:
        self.reset_cooldown = (3 * (1 / 1.2)) ** (self.level - 1)
        if time.time() - self.reset_time >= self.reset_cooldown:
            self.reset_time = time.time()
            return True
        return False

    def periodic(self, player_coordinates: tuple[int, int]) -> None:
        reset = self.get_reset_time()

        if self.x > player_coordinates[0] + 20: # if player is more than 20 pixels right, increases x
            self.x += 3
        elif self.x < player_coordinates[0] - 20:
            self.x -= 3
        elif player_coordinates[1] < 75 and reset: # if player is close to the ground, zombie will hit

