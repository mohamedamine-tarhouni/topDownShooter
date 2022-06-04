import pygame
import pygame_menu
import settings as stn
import model.menu as mn
import model.database as db
# import main
from pygame_menu.examples import create_example_window


def displayScore(player, textColor=stn.BLUE, bgColor=stn.GREEN):
    font = pygame.font.Font('freesansbold.ttf', 32)
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(player.name+" : "+str(player.score),
                       True, bgColor, textColor)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    return textRect, text


def displayHp(player, textColor=stn.BLUE, bgColor=stn.GREEN):
    font = pygame.font.Font('freesansbold.ttf', 32)
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render("HP : "+str(player.HP), True, bgColor, textColor)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    return textRect, text

# def displayScoreBoard():
