import gameData

def upgrade(type):

    if type == "damage":
        gameData.bulletDamage += 5
    elif type == "fireRate":
        gameData.firerate += 100
    elif type == "regeneration":
        pass