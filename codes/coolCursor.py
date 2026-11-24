import pygame
import settings

angle = 0
lastTime = pygame.time.get_ticks()
spinUntil = 0

def quickSpin():
    global spinUntil
    spinUntil = pygame.time.get_ticks() + 400

def update():
    global angle, lastTime

    mouseX, mouseY = pygame.mouse.get_pos()

    lineWidth, lineHeight = 20, 3

    cursor = pygame.Surface((lineWidth, lineWidth), pygame.SRCALPHA)

    pygame.draw.rect(cursor, (255, 255, 255), (0, lineWidth//2-lineHeight//2, lineWidth, lineHeight))
    pygame.draw.rect(cursor, (255, 255, 255), (lineWidth//2-lineHeight//2, 0, lineHeight, lineWidth))

    currentTime = pygame.time.get_ticks()
    dt = (currentTime - lastTime) / 1000
    lastTime = currentTime

    spinSpeed = 30

    if currentTime < spinUntil:
        spinSpeed = 900

    angle += spinSpeed * dt

    cursor = pygame.transform.rotate(cursor, angle)
    cursorRect = cursor.get_rect(center=(mouseX, mouseY))
    settings.screen.blit(cursor, cursorRect)