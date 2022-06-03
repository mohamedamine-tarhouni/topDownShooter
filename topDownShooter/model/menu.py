import pygame_menu
from pygame_menu.examples import create_example_window

from settings import BLUE, GREEN, HEIGHT, WIDTH,player1,player2
# from main import start_the_game



def menuPrincipal(funcStart):
    change_Player1_menu=changePlayer1()
    change_Player2_menu=changePlayer2()
    menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT,
                        theme=pygame_menu.themes.THEME_BLUE)
    
#     menu.add.text_input('Name :', default='',onchange=changeMyPlayerName)
    # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add.button('Play', funcStart)
    menu.add.button('Change Player 1', change_Player1_menu)
    menu.add.button('Change Player 2', change_Player2_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    surface = create_example_window('TopDownShooter', (WIDTH, HEIGHT))
    menu.mainloop(surface)
def changePlayer1():
    change_Player1_menu = pygame_menu.Menu(player1.name, WIDTH, HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE)
    change_Player1_menu.add.text_input('Name :', default=player1.name,onchange=changePlayer1Name)
    change_Player1_menu.add.button('Changer', pygame_menu.events.BACK)
    return change_Player1_menu
def changePlayer2():
    change_Player2_menu = pygame_menu.Menu(player2.name, WIDTH, HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE)
    change_Player2_menu.add.text_input('Name :', default=player2.name,onchange=changePlayer2Name)
    change_Player2_menu.add.button('Changer', pygame_menu.events.BACK)
    return change_Player2_menu
def changePlayer1Name(name):
    player1.name=name
    #on input change your value is returned here
    print('Player name is', player1.name)
def changePlayer2Name(name):
    player2.name=name
    #on input change your value is returned here
    print('Player name is', player2.name)


