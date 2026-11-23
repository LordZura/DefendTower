
import pygame
import math
import random

pygame.init()

pygame.font.init()
font = pygame.font.Font(None, 36)
menuFont = pygame.font.Font(None, 30)
buttonFont = pygame.font.Font(None, 24)

screenX = 800
screenY = 800
menuX = 200
windowX = screenX + menuX

# prepare stuff
screen = pygame.display.set_mode((windowX, screenY))
pygame.display.set_caption("Defend Tower")

running = True

playerX = screenX // 2
playerY = screenY // 2

# bullets
bullets = []
bulletRadius = 7
bulletSpeed = 10
bulletOffset = 25
bulletDamage = 1

# enemies
enemies = []
enemySpawnDistance = 800

currentWave = 1
currentWaveProgressing = False
progressingMultiplier = 1.3
firstWaveMinimum = 10

firerate = 1000
lastShot = 0

points = 0


def render():
    pygame.draw.circle(screen, (0, 150, 255), (playerX, playerY), 20)
    drawBullets()
    drawEnemy()

    waveText = font.render(f"Wave: {currentWave}", True, (255, 255, 255))
    pointsText = font.render(f"Points: {points}", True, (255, 255, 255))

    displayText(waveText, pointsText)
    drawMenu()


def shoot():
    mouseX, mouseY = pygame.mouse.get_pos()

    distanceX = mouseX - playerX
    distanceY = mouseY - playerY

    angle = math.atan2(distanceY, distanceX)

    offsetX = math.cos(angle) * bulletOffset
    offsetY = math.sin(angle) * bulletOffset

    bulletX = playerX + offsetX
    bulletY = playerY + offsetY

    bullets.append([bulletX, bulletY, angle])


def waves():
    global currentWaveProgressing

    if not currentWaveProgressing:
        currentWaveProgressing = True

        enemyAmount = int(firstWaveMinimum * (progressingMultiplier ** (currentWave - 1)))

        for i in range(enemyAmount):
            createEnemy()


def createEnemy():
    enemySpeed = 0.5
    enemyHealth = 3
    enemyRadius = 20
    enemyPoints = 5

    angle = random.uniform(0, 2 * math.pi)
    enemyDistance = random.uniform(enemySpawnDistance, enemySpawnDistance * 2.2)

    enemyX = playerX + math.cos(angle) * enemyDistance
    enemyY = playerY + math.sin(angle) * enemyDistance

    distanceX = playerX - enemyX
    distanceY = playerY - enemyY

    moveAngle = math.atan2(distanceY, distanceX)

    enemies.append({
        'x': enemyX,
        'y': enemyY,
        'speed': enemySpeed,
        'health': enemyHealth,
        'radius': enemyRadius,
        'angle': moveAngle,
        'points': enemyPoints
    })


def drawEnemy():
    for enemy in enemies:
        angle = enemy['angle']
        speed = enemy['speed']

        movementX = math.cos(angle) * speed
        movementY = math.sin(angle) * speed

        enemyX = enemy['x']
        enemyY = enemy['y']

        enemyX += movementX
        enemyY += movementY

        pygame.draw.circle(screen, (255, 0, 0),
                           (int(enemyX), int(enemyY)), enemy['radius'])

        enemy['x'] = enemyX
        enemy['y'] = enemyY


def drawBullets():
    for bullet in bullets:
        angle = bullet[2]

        movementX = math.cos(angle) * bulletSpeed
        movementY = math.sin(angle) * bulletSpeed

        bulletX, bulletY = bullet[0], bullet[1]

        pygame.draw.circle(screen, (0, 255, 255),
                           (int(bulletX), int(bulletY)), bulletRadius)

        bulletX += movementX
        bulletY += movementY

        bullet[0] = bulletX
        bullet[1] = bulletY


def bulletCollision():
    global points

    for bullet in bullets[:]:
        bulletX = bullet[0]
        bulletY = bullet[1]

        for enemy in enemies[:]:
            enemyX = enemy['x']
            enemyY = enemy['y']

            distanceX = bulletX - enemyX
            distanceY = bulletY - enemyY

            distance = math.sqrt(distanceX ** 2 + distanceY ** 2)

            if distance <= bulletRadius + enemy['radius']:
                enemy['health'] -= bulletDamage
                bullets.remove(bullet)

                if enemy['health'] <= 0:
                    enemies.remove(enemy)
                    points += enemy['points']

                break


def displayText(waveText, pointsText):
    screen.blit(waveText, (20, 20))

    pointsX = screenX - pointsText.get_width() - 20
    screen.blit(pointsText, (pointsX, 20))


def drawMenu():
    pygame.draw.rect(screen, (35, 35, 42), (screenX, 0, menuX, screenY))

    pygame.draw.line(screen, (100, 100, 110),
                     (screenX, 0), (screenX, screenY), 2)

    menuTitle = menuFont.render("UPGRADES", True, (255, 255, 255))
    screen.blit(menuTitle, (screenX + 35, 30))

    # upgrade buttons
    drawButton("Increase Damage", screenX + 15, 100)
    drawButton("Increase Fire Rate", screenX + 15, 180)
    drawButton("Regeneration", screenX + 15, 260)


def drawButton(buttonText, buttonX, buttonY):
    buttonWidth = 170
    buttonHeight = 55

    # button background
    pygame.draw.rect(screen, (55, 55, 65),
                     (buttonX, buttonY, buttonWidth, buttonHeight),
                     border_radius=8)

    # button border
    pygame.draw.rect(screen, (100, 100, 115),
                     (buttonX, buttonY, buttonWidth, buttonHeight),
                     2, border_radius=8)

    # button text
    text = buttonFont.render(buttonText, True, (255, 255, 255))

    textX = buttonX + (buttonWidth - text.get_width()) // 2
    textY = buttonY + (buttonHeight - text.get_height()) // 2

    screen.blit(text, (textX, textY))


def removeOffscreenBullets():
    for bullet in bullets[:]:
        bulletX = bullet[0]
        bulletY = bullet[1]

        if (bulletX < -bulletRadius or bulletX > screenX + bulletRadius or
                bulletY < -bulletRadius or bulletY > screenY + bulletRadius):
            bullets.remove(bullet)


clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouseHeld = pygame.mouse.get_pressed()

    if mouseHeld[0]:
        currentTime = pygame.time.get_ticks()
        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseX < screenX and currentTime - lastShot >= firerate:
            shoot()
            lastShot = currentTime

    screen.fill((25, 25, 30))

    render()

    bulletCollision()
    removeOffscreenBullets()

    pygame.display.flip()

    waves()

    if len(enemies) == 0 and currentWaveProgressing:
        currentWave += 1
        currentWaveProgressing = False

    clock.tick(60)

pygame.quit()
