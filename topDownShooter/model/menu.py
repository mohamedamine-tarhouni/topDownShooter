import pygame_menu
from pygame_menu.examples import create_example_window
import model.database as db

from settings import BLUE, GREEN, HEIGHT, WIDTH,player1,player2
# from main import start_the_game



def menuPrincipal(funcStart,loop):
    ScoreBoard=displayScoreBoard()
    change_Player1_menu=changePlayer(player1)
    change_Player2_menu=changePlayer(player2)
    menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT,
                        theme=pygame_menu.themes.THEME_BLUE)
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
def changePlayer(player):
    change_Player_menu = pygame_menu.Menu(player.name, WIDTH, HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE)
    change_Player_menu.add.text_input('Name :', default=player.name,onchange=player.changeName)
    change_Player_menu.add.text_input('MAXHP :', default=str(player.maxHP),onchange=player.changePlayerHP)
    change_Player_menu.add.text_input('Damage :', default=str(player.Dmg),onchange=player.changePlayerDamage)
    change_Player_menu.add.text_input('Attack Speed :', default=str(player.atkSpeed),onchange=player.changePlayeratkspd)
    change_Player_menu.add.text_input('Lives :', default=str(player.lives),onchange=player.changePlayerLives)
    change_Player_menu.add.text_input('Speed :', default=str(player.speed),onchange=player.changePlayerSpeed)
    change_Player_menu.add.button('Changer', pygame_menu.events.BACK)
    return change_Player_menu

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
        displayScoreMenu=scoreOfGame(i[0]+ " : "+str(i[1]),"Score")   
        menu.add.button(i[0]+ " : "+str(i[1]), displayScoreMenu)
    menu.add.button("Menu Principal", pygame_menu.events.BACK)
    # menu.mainloop(surface)
    return menu



