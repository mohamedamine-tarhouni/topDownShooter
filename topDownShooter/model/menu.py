import pygame_menu
from pygame_menu.examples import create_example_window

from settings import BLUE, GREEN, HEIGHT, WIDTH,player1
# from main import start_the_game



def menuPrincipal(funcStart):

    menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT,
                        theme=pygame_menu.themes.THEME_BLUE)
    
#     menu.add.text_input('Name :', default='',onchange=changeMyPlayerName)
    # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add.button('Play', funcStart)
    # menu.add.button('Change Player 1', changePlayer1)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    surface = create_example_window('TopDownShooter', (WIDTH, HEIGHT))
    menu.mainloop(surface)
def changePlayer1():
    menu = pygame_menu.Menu(player1.name, WIDTH, HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('Name :', default=player1.name,onchange=changeMyPlayer1Name)
    menu.add.button('Changer', menuPrincipal())
    surface = create_example_window('TopDownShooter', (WIDTH, HEIGHT))
    menu.mainloop(surface)
def changeMyPlayer1Name(name):
    player1.name=name
    #on input change your value is returned here
    print('Player name is', player1.name)


