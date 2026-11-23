import pygame
import math

pygame.init()

screenX = 800
screenY = 600

# prepare stuff
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Defend Tower")

running = True

playerX = screenX // 2
playerY = screenY // 2

bullets = []
bulletRadius = 7

def shoot():
    mouseX, mouseY = pygame.mouse.get_pos()
    bulletX = playerX
    bulletY = playerY
    bullets.append((bulletX, bulletY))

    createBullet(bulletX, bulletY)

    print(f"you clicked at: X: {mouseX} Y: {mouseY}")
    print(f"bullet created at: X: {bulletX} Y: {bulletY}")

def createBullet(bulletX, bulletY):
    for bullet in bullets:
        pygame.draw.circle(screen, (0, 255, 255), (bullet[0], bullet[1]), bulletRadius)

while running:
    # check if player exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot()

    # filling screen
    screen.fill((25, 25, 30))
    pygame.draw.circle(screen, (0, 150, 255), (playerX, playerY), 20)
    pygame.display.flip()
    
