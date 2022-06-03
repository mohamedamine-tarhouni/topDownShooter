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
def scoreEndGame(str):
    menu = pygame_menu.Menu('Game Over', stn.WIDTH, stn.HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE,)
    menu.add.button(str, displayGameOver)
    return menu



def displayGameOver(textColor=stn.BLUE, bgColor=stn.GREEN):
    menu = pygame_menu.Menu('Scores', stn.WIDTH, stn.HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE,)
    surface = create_example_window('TopDownShooter', (stn.WIDTH, stn.HEIGHT))
    scores=db.getScores()
    for i in scores:
        change_Player1_menu=scoreEndGame(i[0]+ " : "+str(i[2])+", "+i[1]+" : "+str(i[3]))   
        menu.add.button(i[0]+ " : "+str(i[2])+", "+i[1]+" : "+str(i[3]), change_Player1_menu)
        menu.add.button("home", pygame_menu.events.RESET)
    menu.mainloop(surface)
