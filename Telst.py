import pygame
import sys
from Utils import Player

pygame.init()

# 2. Set up the display
WIDTH, HEIGHT = 1080, 720
MOVEMENT_SPEED = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
player = Player(100, 100, 30, 50)

# 3. Create a clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

# 4. Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Handle inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        #move left
        player.x -= MOVEMENT_SPEED
    if keys[pygame.K_d]:
        #move right
        player.x += MOVEMENT_SPEED
    if keys[pygame.K_w]:
        #move up
        player.y -= MOVEMENT_SPEED
    if keys[pygame.K_s]:
        #move down
        player.y += MOVEMENT_SPEED

    #Update
    player.upd_pos()

    #Render
    screen.fill("BLACK")
    player.draw(screen)
    pygame.display.flip()

    clock.tick(FPS) # Limit fps 

pygame.quit()
sys.exit