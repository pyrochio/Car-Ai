import pygame
import sys
from CarPhysics import CarPhysics
from Road import Road
from Player import Player

pygame.init()

WIDTH, HEIGHT = 1440, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
physics = CarPhysics(100, 100, 1000) #heavier = slower acceleration, slower turning, higher max speed
#1000 low 4000 high
player = Player(30, 50)
road = Road(250, 500, mu_k=0.005, mu_s=0.5, lane_count=4)

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    throttle = int(keys[pygame.K_w]) - int(keys[pygame.K_s])
    steering = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    drifting = keys[pygame.K_SPACE]

    #delta time in seconds caps fps to 60
    # actual seconds this frame took
    dt = clock.tick(FPS) / 1000

    physics.update(
        throttle=throttle,
        steering=steering,
        dt=dt,
        mu_k=road.mu_k,
        mu_s=road.mu_s,
        drifting=drifting,
    )

    screen.fill("BLACK")
    road.draw(screen)
    player.draw(screen, physics.x, physics.y, physics.angle, drifting, dt)
    pygame.display.flip()


pygame.quit()
sys.exit()
