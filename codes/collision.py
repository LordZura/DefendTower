import math

import settings
import gameData


def bulletCollision():
    # checks every bullet against every enemy
    for bullet in gameData.bullets[:]:
        bulletX = bullet[0]
        bulletY = bullet[1]

        for enemy in gameData.enemies[:]:
            enemyX = enemy['x']
            enemyY = enemy['y']

            distanceX = bulletX - enemyX
            distanceY = bulletY - enemyY

            distance = math.sqrt(distanceX ** 2 + distanceY ** 2)

            # checks if the bullet touches the enemy
            if distance <= settings.bulletRadius + enemy['radius']:
                enemy['health'] -= gameData.bulletDamage
                gameData.bullets.remove(bullet)

                # removes enemy when its health reaches zero
                if enemy['health'] <= 0:
                    gameData.enemies.remove(enemy)
                    gameData.points += enemy['points']

                # one bullet can only hit one enemy
                break