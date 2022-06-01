import pygame
from settings import BLUE, GREEN
def displayScore(player,textColor=BLUE,bgColor=GREEN):
        font = pygame.font.Font('freesansbold.ttf', 32)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render(player.name+" : "+str(player.score), True, bgColor, textColor)
        
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        return textRect,text
def displayHp(player,textColor=BLUE,bgColor=GREEN):
        font = pygame.font.Font('freesansbold.ttf', 32)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render("HP : "+str(player.HP), True, bgColor, textColor)
        
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        return textRect,text