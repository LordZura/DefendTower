import pygame
import settings

def update():
    mouseX,mouseY = pygame.mouse.get_pos()
    lineWidth,lineHeight = 20,3
    
    pygame.draw.rect(settings.screen, (255, 255, 255), (mouseX-lineWidth//2, mouseY-lineHeight//2, lineWidth, lineHeight))
    pygame.draw.rect(settings.screen, (255, 255, 255), (mouseX-lineHeight//2, mouseY-lineWidth//2, lineHeight, lineWidth))

    