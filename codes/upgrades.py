import gameData

def upgrade(type):

    if type == "damage":
        gameData.bulletDamage += 5
    elif type == "firerate":
        gameData.firerate *= 0.9
    elif type == "regeneration":
        pass
    elif type == "penetration":
        gameData.penetration += 1