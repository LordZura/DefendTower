import settings

# player
playerX = settings.screenX // 2
playerY = settings.screenY // 2

# bullets
bullets = []
bulletDamage = 1
penetration = 0

# enemies
enemies = []

currentWave = 1
currentWaveProgressing = False

firerate = 1000
lastShot = 0

points = 0

enemyStats = {}
enemyStats = settings.enemyStartingStats

enemyDifficulty = 1