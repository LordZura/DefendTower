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
bulletSpeed = 10

def render():
    pygame.draw.circle(screen, (0, 150, 255), (playerX, playerY), 20)
    drawBullets()

def shoot():
    mouseX, mouseY = pygame.mouse.get_pos()
    bulletX = playerX
    bulletY = playerY

    distanceX = mouseX - playerX
    distanceY = mouseY - playerY

    angle = math.atan2(distanceY, distanceX)

    bullets.append([bulletX, bulletY, angle])

    print(f"you clicked at: X: {mouseX} Y: {mouseY}")
    print(f"bullet created at: X: {bulletX} Y: {bulletY}")

def drawBullets():
    for bullet in bullets:
        angle = bullet[2]
        movementX = math.cos(angle) * bulletSpeed
        movementY = math.sin(angle) * bulletSpeed

        bulletX,bulletY = bullet[0],bullet[1]

        pygame.draw.circle(screen, (0, 255, 255), (bulletX, bulletY), bulletRadius)

        bulletX += movementX
        bulletY += movementY

        bullet[0] = bulletX
        bullet[1] = bulletY

while running:
    # check if player exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot()

    # filling screen
    screen.fill((25, 25, 30))
    render()
    pygame.display.flip()
    
