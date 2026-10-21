import pygame
import sys
import math

#this class is not used in the current implementation, but it can be used to handle player controls in the future.
# class Controls:
#     def __init__(self):
#         self.forward = False
#         self.backward = False
#         self.left = False
#         self.right = False
    
class Player:
    def __init__(self, x, y, w, h):
        self.color = "ORANGE"
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center=(self.x, self.y))

        self.speed = 0
        self.acceleration = 0.2
        self.friction = 0.05
        self.max_speed = 10
        self.angle = 0

    def upd_pos(self):
        #directional movement based on angle angles are rotated 90 degrees counterclockwise from the standard Cartesian coordinate system
        self.y += self.speed * math.cos(self.angle)
        self.x += self.speed * math.sin(self.angle)

        self.rect = self.surf.get_rect(center=(self.x, self.y))

        #checks max speeds
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        #applies friction
        if self.speed > 0:
            self.speed -= self.friction
        if self.speed < 0:
            self.speed += self.friction
        if abs(self.speed) < self.friction:
            self.speed = 0

    def draw(self, screen):
        rotated = pygame.transform.rotozoom(self.surf, math.degrees(self.angle), 1)
        rect = rotated.get_rect(center=self.rect.center)
        screen.blit(rotated, rect)