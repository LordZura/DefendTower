import pygame

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

# bullets
bulletRadius = 7
bulletSpeed = 10
bulletOffset = 25

# enemies
enemySpawnDistance = 800
progressingMultiplier = 1.5
firstWaveMinimum = 50

# menu
menuBackground = (35, 35, 42)
buttonColor = (55, 55, 65)
buttonBorder = (100, 100, 115)
menuTextColor = (255, 255, 255)
buttonOffset = 15
buttonGap = 80

button1Cost = 20
button2Cost = 20
button3Cost = 20
button4Cost = 20

buttonCostMultiplier = 1.3

enemyStartingStats = {
    "speed": 0.3,
    "health": 20,
    "damage": 5
}

enemyDifficultyMultiplier = 1.8

regenTime = 1000