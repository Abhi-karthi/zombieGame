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
        self.y = 75
        self.reset_time = time.time()
        self.reset_cooldown = 3
        self.state = "walking"
        self.damage = 0
        self.dead_timer = 0
        self.dead = False
        self.health = self.level * 30
        self.face = "left"
        # size of screen: 1920x1050

    def get_reset_time(self) -> bool:
        self.reset_cooldown = (3 * (1 / 1.2)) ** (self.level - 1)
        if time.time() - self.reset_time >= self.reset_cooldown:
            self.reset_time = time.time()
            return True
        return False

    def periodic(self, player_coordinates: tuple[int, int]) -> None:
        reset = self.get_reset_time()
        if self.health <= 0 and self.dead_timer != 0:
            self.state = "dead"
            self.dead_timer = time.time()
        else:
            if self.x > player_coordinates[0] + 20:  # if player is more than 20 pixels right, increases x
                self.x += 3
                self.damage = 0
                self.state = "walking"
                self.face = "right"
            elif self.x < player_coordinates[0] - 20:
                self.x -= 3
                self.damage = 0
                self.state = "walking"
                self.face = "left"
            elif player_coordinates[1] < 75 and reset:  # if player is close to the ground, zombie will hit
                self.damage = self.level * 2
                self.state = "attacking"
            elif player_coordinates[1] < 75:
                self.damage = 0
                self.state = "attacking"
            else:
                self.state = "idle"
                self.damage = 0

        if time.time() - self.dead_timer > 1:  # waits for one second after death to delete zombie
            self.dead = True
