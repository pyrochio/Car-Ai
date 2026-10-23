import pygame
from math import *
from Utils import *

ROAD_COLOR = "GREY"
class Road:
    def __init__(self, x, width, mu_k, mu_s, lane_count=4):
        self.x = x
        self.width = width
        self.lane_count = lane_count
        self.mu_k = mu_k
        self.mu_s = mu_s

        self.left = x - width / 2
        self.right = x + width / 2

        infinity = 1000000
        self.top = -infinity
        self.bottom = infinity

        top_left = (self.left, self.top)
        top_right = (self.right, self.top)
        bottom_left = (self.left, self.bottom)
        bottom_right = (self.right, self.bottom)

        self.borders = [
            [top_left, bottom_left],
            [top_right, bottom_right]
        ]

    def draw(self, screen):
        pygame.draw.line(screen, "WHITE", (self.left, self.top), (self.left, self.bottom), 10)
        pygame.draw.line(screen, "WHITE", (self.right, self.top), (self.right, self.bottom), 10)
        for i in range(1, self.lane_count):
            x = lerp(self.left, self.right, i / self.lane_count)
            pygame.draw.line(screen, "GRAY", (x, self.top), (x, self.bottom), 5)
            