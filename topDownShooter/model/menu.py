import pygame_menu
from pygame_menu.examples import create_example_window
import model.database as db

from settings import BLUE, GREEN, HEIGHT, WIDTH,player1,player2
# from main import start_the_game



def menuPrincipal(funcStart,loop):
    ScoreBoard=displayScoreBoard()
    change_Player1_menu=changePlayer1()
    change_Player2_menu=changePlayer2()
    menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT,
                        theme=pygame_menu.themes.THEME_BLUE)
    
#     menu.add.text_input('Name :', default='',onchange=changeMyPlayerName)
    # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add.button('Play', funcStart)
    menu.add.button('Change Player 1', change_Player1_menu)
    menu.add.button('Change Player 2', change_Player2_menu)
    menu.add.button('High Scores', ScoreBoard)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    surface = create_example_window('TopDownShooter', (WIDTH, HEIGHT))
    if loop:
        menu.mainloop(surface)
    else:
        return menu
def changePlayer1():
    change_Player1_menu = pygame_menu.Menu(player1.name, WIDTH, HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE)
    change_Player1_menu.add.text_input('Name :', default=player1.name,onchange=player1.changeName)
    change_Player1_menu.add.text_input('MAXHP :', default=str(player1.maxHP),onchange=player1.changePlayerHP)
    change_Player1_menu.add.text_input('Damage :', default=str(player1.Dmg),onchange=player1.changePlayerDamage)
    change_Player1_menu.add.text_input('Attack Speed :', default=str(player1.atkSpeed),onchange=player1.changePlayeratkspd)
    change_Player1_menu.add.text_input('Lives :', default=str(player1.lives),onchange=player1.changePlayerLives)
    change_Player1_menu.add.button('Changer', pygame_menu.events.BACK)
    return change_Player1_menu
def changePlayer2():
    change_Player2_menu = pygame_menu.Menu(player2.name, WIDTH, HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE)
    change_Player2_menu.add.text_input('Name :', default=player2.name,onchange=player2.changeName)
    change_Player2_menu.add.text_input('MAXHP :', default=str(player2.maxHP),onchange=player2.changePlayerHP)
    change_Player2_menu.add.text_input('Damage :', default=str(player2.Dmg),onchange=player2.changePlayerDamage)
    change_Player2_menu.add.text_input('Attack Speed :', default=str(player2.atkSpeed),onchange=player2.changePlayeratkspd)
    change_Player2_menu.add.text_input('Lives :', default=str(player2.lives),onchange=player2.changePlayerLives)
    change_Player2_menu.add.button('Changer', pygame_menu.events.BACK)
    return change_Player2_menu

def scoreOfGame(str,title):
    menu = pygame_menu.Menu(title, WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE,)
    menu.add.button(str, displayScoreBoard)
    return menu
def scoreEndGame(funcStart,str):
    menu_Principal=menuPrincipal(funcStart,False)
    menu = pygame_menu.Menu("Game Over", WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE,)
    surface = create_example_window('TopDownShooter', (WIDTH, HEIGHT))
    # menu.add.button("Menu Principal", menuPrincipal(funcStart))
    menu.add.button(str, )
    menu.add.button("Menu Principal", menu_Principal)
    menu.mainloop(surface)



def displayScoreBoard():
    menu = pygame_menu.Menu('Score Board', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE,)
    # surface = create_example_window('TopDownShooter', (WIDTH, HEIGHT))
    scores=db.getScores()
    for i in scores:
        displayScoreMenu=scoreOfGame(i[0]+ " : "+str(i[2])+", "+i[1]+" : "+str(i[3]),"Score")   
        menu.add.button(i[0]+ " : "+str(i[2])+", "+i[1]+" : "+str(i[3]), displayScoreMenu)
    menu.add.button("home", pygame_menu.events.BACK)
    # menu.mainloop(surface)
    return menu



