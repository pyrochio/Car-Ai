import pygame
import math


class Player:
    def __init__(self, w, h):
        self.color = "ORANGE"
        self.width = w
        self.height = h
        self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surf.fill(self.color)
        self.trails = None
        self.previous_rear_tires = None
        self.trail_lifetime = 5.0

    def draw(self, screen, x, y, angle, drifting, dt):
        #create a new surface for the trails if it doesn't exist 
        if self.trails is None or self.trails.get_size() != screen.get_size():
            self.trails = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

        #fade the trails over time
        fade = math.pow(0.01, max(0.0, dt) / self.trail_lifetime)
        self.trails.fill((255, 255, 255, round(fade * 255)), special_flags=pygame.BLEND_RGBA_MULT,)

        if drifting:
            #get drift marks
            forward_x = math.sin(angle)
            forward_y = -math.cos(angle)
            right_x = math.cos(angle)
            right_y = math.sin(angle)

            #get tire positions
            rear_offset = self.height * 0.35
            tire_offset = self.width * 0.38

            rear_x = x - forward_x * rear_offset
            rear_y = y - forward_y * rear_offset
            rear_tires = (
                (rear_x - right_x * tire_offset, rear_y - right_y * tire_offset),
                (rear_x + right_x * tire_offset, rear_y + right_y * tire_offset),
            )

            #draw lines from previous tire positions to current tire positions
            if self.previous_rear_tires is not None:
                for previous, current in zip(self.previous_rear_tires, rear_tires):
                    pygame.draw.line(self.trails, (45, 45, 45, 220),
                        (round(previous[0]), round(previous[1])),
                        (round(current[0]), round(current[1])),
                        4,)
            self.previous_rear_tires = rear_tires

        else:
            self.previous_rear_tires = None

        #draw the trails and the car
        screen.blit(self.trails, (0, 0))
        rotated = pygame.transform.rotozoom(self.surf, -math.degrees(angle), 1)
        rect = rotated.get_rect(center=(x, y))
        screen.blit(rotated, rect)