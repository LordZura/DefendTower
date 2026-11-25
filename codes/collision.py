import math

import settings
import gameData
import sounds

def bulletCollision():
    # checks every bullet against every enemy
    for bullet in gameData.bullets[:]:
        bulletX = bullet[0]
        bulletY = bullet[1]

        for enemy in gameData.enemies[:]:

            # checks if this bullet has already hit this enemy
            if any(hitEnemy is enemy for hitEnemy in bullet[4]):
                continue

            enemyX = enemy['x']
            enemyY = enemy['y']

            distanceX = bulletX - enemyX
            distanceY = bulletY - enemyY

            distance = math.sqrt(distanceX ** 2 + distanceY ** 2)

            # checks if the bullet touches the enemy
            if distance <= settings.bulletRadius + enemy['radius']:

                # remembers that this bullet hit this enemy
                bullet[4].append(enemy)

                enemy['health'] -= gameData.bulletDamage
                sounds.playSound(sounds.hitSound)


                # checks bullet penetration
                if bullet[3] >= 1:
                    bullet[3] -= 1
                else:
                    gameData.bullets.remove(bullet)

                # removes enemy when its health reaches zero
                if enemy['health'] <= 0:
                    gameData.enemies.remove(enemy)
                    gameData.points += enemy['points']
                    sounds.playSound(sounds.killSound)

                # one bullet can only hit one new enemy per frame
                break


def enemyCollision():
    for enemy in gameData.enemies[:]:
        distanceX = gameData.playerX - enemy['x']
        distanceY = gameData.playerY - enemy['y']

        distance = math.sqrt(distanceX ** 2 + distanceY ** 2)

        if distance <= 25 + enemy['radius']:
            gameData.playerHealth -= enemy['damage']