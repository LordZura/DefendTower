import pygame
import math
import random

pygame.init()

screenX = 800
screenY = 800

# prepare stuff
screen = pygame.display.set_mode((screenX, screenY))
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

def render():
    # renders everything
    pygame.draw.circle(screen, (0, 150, 255), (playerX, playerY), 20)
    drawBullets()
    drawEnemy()

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


def waves():
    global currentWaveProgressing

    if not currentWaveProgressing:
        currentWaveProgressing = True

        for i in range(firstWaveMinimum):
            createEnemy()

def createEnemy():
    enemySpeed = 0.5
    enemyHealth = 3
    enemyRadius = 20

    angle = random.uniform(0, 2*math.pi)
    enemyDistance = enemySpawnDistance * random.uniform(0.9, 2.2)

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
        'angle': moveAngle
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

        enemyRadius = enemy['radius']
        pygame.draw.circle(screen, (255, 0, 0), (int(enemyX), int(enemyY)), enemyRadius)

        enemy['x'] = enemyX
        enemy['y'] = enemyY
    
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

clock = pygame.time.Clock()

while running:
    # check if player exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    mouseHeld = pygame.mouse.get_pressed()

    if mouseHeld[0]:
        currentTIme = pygame.time.get_ticks()

        if currentTIme - lastShot >= firerate:
            shoot()
            lastShot = currentTIme

    # filling screen
    screen.fill((25, 25, 30))
    render()
    pygame.display.flip()

    waves()
    if len(enemies) == 0 and currentWaveProgressing:
        currentWave += 1
        currentWaveProgressing = False

    # fps limiter
    clock.tick(60)


