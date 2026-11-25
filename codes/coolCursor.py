import pygame
import settings
import gameData

angle = 0
lastTime = pygame.time.get_ticks()
spinUntil = 0

cursorSize = 20
targetSize = 20

def quickSpin():
    global spinUntil
    spinUntil = pygame.time.get_ticks() + 400

def update():
    global angle, lastTime, cursorSize, targetSize

    mouseX, mouseY = pygame.mouse.get_pos()

    currentTime = pygame.time.get_ticks()
    dt = (currentTime - lastTime) / 1000
    lastTime = currentTime

    if mouseX > settings.screenX:
        targetSize = 35
    else:
        targetSize = 20

    cursorSize += (targetSize - cursorSize) * min(dt * 8, 1)

    spinSpeed = 30

    if currentTime < spinUntil:
        spinSpeed = 900

    angle += spinSpeed * dt

    cursor = pygame.Surface((20, 20), pygame.SRCALPHA)

    pygame.draw.rect(cursor, (255, 255, 255), (0, 9, 20, 3))
    pygame.draw.rect(cursor, (255, 255, 255), (9, 0, 3, 20))

    cursor = pygame.transform.scale(cursor, (int(cursorSize), int(cursorSize)))
    cursor = pygame.transform.rotate(cursor, angle)

    cursorRect = cursor.get_rect(center=(mouseX, mouseY))

    settings.screen.blit(cursor, cursorRect)

    pygame.draw.line(settings.screen, (255, 255, 255), (int(gameData.playerX), (gameData.playerY)), (mouseX, mouseY))