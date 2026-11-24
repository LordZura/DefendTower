import pygame

import settings


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
    drawButton("Increase Damage", settings.screenX + 15, 100)
    drawButton("Increase Fire Rate", settings.screenX + 15, 180)
    drawButton("Regeneration", settings.screenX + 15, 260)


def drawButton(buttonText, buttonX, buttonY):
    buttonWidth = 170
    buttonHeight = 55

    # button background
    pygame.draw.rect(
        settings.screen,
        settings.buttonColor,
        (buttonX, buttonY, buttonWidth, buttonHeight),
        border_radius=8
    )

    # button border
    pygame.draw.rect(
        settings.screen,
        settings.buttonBorder,
        (buttonX, buttonY, buttonWidth, buttonHeight),
        2,
        border_radius=8
    )

    # button text
    text = settings.buttonFont.render(buttonText, True, settings.menuTextColor)

    textX = buttonX + (buttonWidth - text.get_width()) // 2
    textY = buttonY + (buttonHeight - text.get_height()) // 2

    settings.screen.blit(text, (textX, textY))