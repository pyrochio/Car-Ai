import pygame
import sys

#this class is not used in the current implementation, but it can be used to handle player controls in the future.
# class Controls:
#     def __init__(self):
#         self.forward = False
#         self.backward = False
#         self.left = False
#         self.right = False
    
class Player:
    def __init__(self, x, y, w, h):
        self.color = "WHITE"
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    def upd_pos(self):
        # self.x = self.x - self.width // 2 
        # self.y = self.y - self.height // 2        
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.surf, self.rect)