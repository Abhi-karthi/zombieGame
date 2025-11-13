import pygame
import time
import random


class Player:
    def __init__(self, difficulty: int):  # 1 difficulty is easy, 2 is medium, 3 is hard
        if difficulty != 1 and difficulty != 2 and difficulty != 3:
            raise IOError("Difficulty must be 1, 2, or 3")
        self.health = 100 - (difficulty * 15)
        self.state = "idle"
        self.face = "right"
        self.cooldown_percentage = 100
        self.cooldown_timer = time.time() - 0.4
        self.cooldown_time = 0.4
        self.x = 960
        self.y = 75

    def periodic(self, up: bool = False, right: bool = False, left: bool = False, click: bool = False):
        if up:
            pass
        else:
            if right:
                self.x += 3
                self.state = "running"
                self.face = "right"
            if left:
                self.x -= 3
                self.state = "running"
                self.face = "left"

