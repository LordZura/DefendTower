import pygame

import gameData
import upgrades
import settings



buttonWidth = 170
buttonHeight = 55

buttonRect1 = pygame.Rect(settings.screenX + settings.buttonOffset, 100, buttonWidth, buttonHeight)
buttonRect2 = pygame.Rect(settings.screenX + settings.buttonOffset, 100 + settings.buttonGap, buttonWidth, buttonHeight)
buttonRect3 = pygame.Rect(settings.screenX + settings.buttonOffset, 100 + settings.buttonGap*2, buttonWidth, buttonHeight)
buttonRect4 = pygame.Rect(settings.screenX + settings.buttonOffset, 100 + settings.buttonGap*3, buttonWidth, buttonHeight)


def drawMenu():
    # menu background
    pygame.draw.rect(settings.screen, settings.menuBackground, (settings.screenX, 0, settings.menuX, settings.screenY))

    # menu separator
    pygame.draw.line(settings.screen, (100, 100, 110),
                     (settings.screenX, 0), (settings.screenX, settings.screenY), 2)

    # menu title
    menuTitle = settings.menuFont.render("UPGRADES", True, settings.menuTextColor)
    settings.screen.blit(menuTitle, (settings.screenX + 35, 30))

    # upgrade buttons
    drawButton("Increase Damage", settings.screenX + settings.buttonOffset, 100)
    drawButton("Increase Fire Rate", settings.screenX + settings.buttonOffset, 100 + settings.buttonGap)
    drawButton("Regeneration", settings.screenX + settings.buttonOffset, 100 + settings.buttonGap*2)
    drawButton("Penetration", settings.screenX + settings.buttonOffset, 100 + settings.buttonGap*3)


def drawButton(buttonText, buttonX, buttonY):

    # button background
    pygame.draw.rect(
        settings.screen,
        settings.buttonColor,
        (buttonX, buttonY, buttonWidth, buttonHeight)
    )

    # button border
    pygame.draw.rect(
        settings.screen,
        settings.buttonBorder,
        (buttonX, buttonY, buttonWidth, buttonHeight),
        3,
        border_radius = 5
    )

    # button text
    text = settings.buttonFont.render(buttonText, True, settings.menuTextColor)

    textX = buttonX + (buttonWidth - text.get_width()) // 2
    textY = buttonY + (buttonHeight - text.get_height()) // 2

    settings.screen.blit(text, (textX, textY))


def buttonClickCheck():
    mouseXY = pygame.mouse.get_pos()
    
    if buttonRect1.collidepoint(mouseXY):
        if settings.button1Cost <= gameData.points:
            upgrades.upgrade("damage")
            gameData.points -= settings.button1Cost
        else:
            purchaseFailed()
    elif buttonRect2.collidepoint(mouseXY):
        if settings.button2Cost <= gameData.points:
            upgrades.upgrade("firerate")
            gameData.points -= settings.button2Cost
        else:
            purchaseFailed()
    elif buttonRect3.collidepoint(mouseXY):
        if settings.button3Cost <= gameData.points:
            upgrades.upgrade("regeneration")
            gameData.points -= settings.button3Cost
        else:
            purchaseFailed()
    elif buttonRect4.collidepoint(mouseXY):
        if settings.button1Cost <= gameData.points:
            upgrades.upgrade("penetration")
            gameData.points -= settings.button4Cost
        else:
            purchaseFailed()

def purchaseFailed():
    print("cant buy yet")