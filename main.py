import pygame

pygame.init()

screenX = 800
screenY = 600

# prepare stuff
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Defend Tower")

running = True

playerX = screenX // 2
playerY = screenY // 2

# draw stuff


while running:
    # check if player exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # filling screen
    screen.fill((25, 25, 30))
    pygame.draw.circle(screen, (0, 150, 255), (playerX, playerY), 20)
    pygame.display.flip()
    

