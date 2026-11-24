
import math
import pygame

import settings
import gameData


lastRegen = pygame.time.get_ticks()


def shoot():
    # shooting positioning logics
    mouseX, mouseY = pygame.mouse.get_pos()

    distanceX = mouseX - gameData.playerX
    distanceY = mouseY - gameData.playerY

    angle = math.atan2(distanceY, distanceX)

    offsetX = math.cos(angle) * settings.bulletOffset
    offsetY = math.sin(angle) * settings.bulletOffset

    bulletX = gameData.playerX + offsetX
    bulletY = gameData.playerY + offsetY

    life = gameData.penetration

    gameData.bullets.append([bulletX, bulletY, angle, life, []])


def drawBullets():
    # bullet movement logics
    for bullet in gameData.bullets:
        angle = bullet[2]

        movementX = math.cos(angle) * settings.bulletSpeed
        movementY = math.sin(angle) * settings.bulletSpeed

        bulletX, bulletY = bullet[0], bullet[1]

        pygame.draw.circle(
            settings.screen,
            (0, 255, 255),
            (int(bulletX), int(bulletY)),
            settings.bulletRadius
        )

        bulletX += movementX
        bulletY += movementY

        bullet[0] = bulletX
        bullet[1] = bulletY


def removeOffscreenBullets():
    # removes bullets that have travelled far outside the screen
    for bullet in gameData.bullets[:]:
        bulletX = bullet[0]
        bulletY = bullet[1]

        if (bulletX < -settings.bulletRadius or bulletX > settings.screenX + settings.bulletRadius or
                bulletY < -settings.bulletRadius or bulletY > settings.screenY + settings.bulletRadius):
            gameData.bullets.remove(bullet)


def healthCheck():
    global lastRegen

    currentTime = pygame.time.get_ticks()

    # checks if player has regeneration
    if gameData.regen <= 0:
        lastRegen = currentTime
        return

    # checks if player has full health
    if gameData.playerHealth >= gameData.playerMaxHealth:
        gameData.playerHealth = gameData.playerMaxHealth
        lastRegen = currentTime
        return

    # checks if enough time has passed
    if currentTime - lastRegen >= settings.regenTime:
        gameData.playerHealth += gameData.regen

        # prevents health from exceeding maximum health
        gameData.playerHealth = min(gameData.playerHealth, gameData.playerMaxHealth)

        lastRegen = currentTime
