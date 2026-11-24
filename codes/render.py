import pygame

import settings
import gameData
import player
import enemy
import menu


def render():
    # renders everything
    pygame.draw.circle(settings.screen, (0, 150, 255), (gameData.playerX, gameData.playerY), 20)
    player.drawBullets()
    enemy.drawEnemy()

    waveText = settings.font.render(f"Wave: {gameData.currentWave}", True, (255, 255, 255))
    pointsText = settings.font.render(f"Points: {gameData.points}", True, (255, 255, 255))

    displayText(waveText, pointsText)
    menu.drawMenu()


def displayText(waveText, pointsText):
    settings.screen.blit(waveText, (20, 20))

    pointsX = settings.screenX - pointsText.get_width() - 20
    settings.screen.blit(pointsText, (pointsX, 20))