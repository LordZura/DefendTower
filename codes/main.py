import pygame

import coolCursor
import settings
import gameData
import player
import enemy
import collision
import render
import menu
import sounds

running = True
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

while running and not gameData.lost:
    # check if player exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX > settings.screenX:
                menu.buttonClickCheck()

    mouseHeld = pygame.mouse.get_pressed()

    if mouseHeld[0]:
        currentTime = pygame.time.get_ticks()

        mouseX, mouseY = pygame.mouse.get_pos()

        # only shoot inside the game area
        if mouseX < settings.screenX and currentTime - gameData.lastShot >= gameData.firerate:
            player.shoot()
            gameData.lastShot = currentTime
            sounds.playSound(sounds.shootSound)


    # filling screen
    settings.screen.fill((25, 25, 30))

    coolCursor.update()

    render.render()

    collision.bulletCollision()
    player.removeOffscreenBullets()
    collision.enemyCollision()
    player.healthCheck()

    pygame.display.flip()

    enemy.waves()

    if len(gameData.enemies) == 0 and gameData.currentWaveProgressing:
        gameData.currentWave += 1
        gameData.currentWaveProgressing = False

    # fps limiter
    clock.tick(60)

pygame.quit()