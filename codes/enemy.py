import math
import random
import pygame

import settings
import gameData


def waves():
    if not gameData.currentWaveProgressing:
        gameData.currentWaveProgressing = True

        enemyAmount = int(settings.firstWaveMinimum * (settings.progressingMultiplier ** (gameData.currentWave - 1)))

        if gameData.currentWave > 1:
            gameData.enemyDifficulty = settings.enemyDifficultyMultiplier * gameData.currentWave 

        for i in range(enemyAmount):
            createEnemy()


def createEnemy():
    enemySpeed = gameData.enemyStats['speed'] * (gameData.enemyDifficulty * 0.75)
    enemyHealth = gameData.enemyStats['health'] * gameData.enemyDifficulty
    enemyDamage = gameData.enemyStats['damage'] * gameData.enemyDifficulty
    enemyRadius = 20
    enemyPoints = 5

    angle = random.uniform(0, 2 * math.pi)
    enemyDistance = random.uniform(settings.enemySpawnDistance, settings.enemySpawnDistance * 2.2)

    # spawn relative to the center of the screen
    enemyX = gameData.playerX + math.cos(angle) * enemyDistance
    enemyY = gameData.playerY + math.sin(angle) * enemyDistance

    distanceX = gameData.playerX - enemyX
    distanceY = gameData.playerY - enemyY

    moveAngle = math.atan2(distanceY, distanceX)

    gameData.enemies.append({
        'x': enemyX,
        'y': enemyY,
        'speed': enemySpeed,
        'health': enemyHealth,
        'radius': enemyRadius,
        'angle': moveAngle,
        'points': enemyPoints,
        'damage': enemyDamage
    })


def drawEnemy():
    for enemy in gameData.enemies:
        angle = enemy['angle']
        speed = enemy['speed']

        movementX = math.cos(angle) * speed
        movementY = math.sin(angle) * speed

        enemyX = enemy['x']
        enemyY = enemy['y']

        enemyX += movementX
        enemyY += movementY

        enemyRadius = enemy['radius']

        pygame.draw.circle(
            settings.screen,
            (255, 0, 0),
            (int(enemyX), int(enemyY)),
            enemyRadius
        )

        enemy['x'] = enemyX
        enemy['y'] = enemyY