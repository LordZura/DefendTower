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
bulletOffset = 25

firerate = 200
lastShot = 0

def render():
    # renders everything
    pygame.draw.circle(screen, (0, 150, 255), (playerX, playerY), 20)
    drawBullets()

def shoot():
    # shooting positioning logics
    mouseX, mouseY = pygame.mouse.get_pos()

    distanceX = mouseX - playerX
    distanceY = mouseY - playerY

    angle = math.atan2(distanceY, distanceX)

    offsetX = math.cos(angle) * bulletOffset
    offsetY = math.sin(angle) * bulletOffset

    bulletX = playerX + offsetX
    bulletY = playerY + offsetY

    bullets.append([bulletX, bulletY, angle])

def drawBullets():
    # bullet movement logics
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

            currentTIme = pygame.time.get_ticks()

            if currentTIme - lastShot >= firerate:
                shoot()
                lastShot = currentTIme

    # filling screen
    screen.fill((25, 25, 30))
    render()
    pygame.display.flip()

    # fps limiter
    clock = pygame.time.Clock()
    clock.tick(60)
    
