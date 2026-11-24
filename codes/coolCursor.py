import pygame
import settings

def update():
    mouseX, mouseY = pygame.mouse.get_pos()

    lineWidth, lineHeight = 20, 3

    cursor = pygame.Surface((lineWidth, lineWidth), pygame.SRCALPHA)

    pygame.draw.rect(cursor, (255, 255, 255), (0, lineWidth//2-lineHeight//2, lineWidth, lineHeight))
    pygame.draw.rect(cursor, (255, 255, 255), (lineWidth//2-lineHeight//2, 0, lineHeight, lineWidth))

    angle = pygame.time.get_ticks() * 0.03
    cursor = pygame.transform.rotate(cursor, angle)

    cursorRect = cursor.get_rect(center=(mouseX, mouseY))
    settings.screen.blit(cursor, cursorRect)