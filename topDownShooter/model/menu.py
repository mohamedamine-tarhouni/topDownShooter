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
    change_Player1_menu.add.text_input('Name :', default=player1.name,onchange=changePlayer1Name)
    change_Player1_menu.add.text_input('MAXHP :', default=str(player1.maxHP),onchange=changePlayer1HP)
    change_Player1_menu.add.text_input('Damage :', default=str(player1.Dmg),onchange=changePlayer1Damage)
    change_Player1_menu.add.text_input('Attack Speed :', default=str(player1.atkSpeed),onchange=changePlayer1atkspd)
    change_Player1_menu.add.text_input('Lives :', default=str(player1.lives),onchange=changePlayer1Lives)
    change_Player1_menu.add.button('Changer', pygame_menu.events.BACK)
    return change_Player1_menu
def changePlayer2():
    change_Player2_menu = pygame_menu.Menu(player2.name, WIDTH, HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE)
    change_Player2_menu.add.text_input('Name :', default=player2.name,onchange=changePlayer2Name)
    change_Player2_menu.add.text_input('MAXHP :', default=str(player2.maxHP),onchange=changePlayer2HP)
    change_Player2_menu.add.text_input('Damage :', default=str(player2.Dmg),onchange=changePlayer2Damage)
    change_Player2_menu.add.text_input('Attack Speed :', default=str(player2.atkSpeed),onchange=changePlayer2atkspd)
    change_Player2_menu.add.text_input('Lives :', default=str(player2.lives),onchange=changePlayer2Lives)
    change_Player2_menu.add.button('Changer', pygame_menu.events.BACK)
    return change_Player2_menu

    #traitement des données du joueur1

    #changement de nom
def changePlayer1Name(name):
    player1.name=name
    #on input change your value is returned here
    print('Player name is', player1.name)
    db.insertValue(player1,1)

    #changement de dégat
def changePlayer1Damage(dmg):
    player1.Dmg=int(dmg)
    #on input change your value is returned here
    print('Player damage is', player1.Dmg)
    db.insertValue(player1,1)



    #changement de points de vie
def changePlayer1HP(HP):
    player1.maxHP=float(HP)
    #on input change your value is returned here
    print('Player health is', player1.maxHP)
    db.insertValue(player1,1)

    #changement de vitesse d'attaque
def changePlayer1atkspd(atkspd):
    player1.atkSpeed=int(atkspd)
    #on input change your value is returned here
    print('Player attack speed is', player1.atkSpeed)
    db.insertValue(player1,1)


    #changement de nombre de vies
def changePlayer1Lives(lives):
    player1.lives=int(lives)
    #on input change your value is returned here
    print('Player lives is', player1.lives)
    db.insertValue(player1,1)
def changePlayer2Name(name):
    player2.name=name
    #on input change your value is returned here
    print('Player name is', player2.name)
    db.insertValue(player2,2)



    #changement de dégat
def changePlayer2Damage(dmg):
    player2.Dmg=int(dmg)
    #on input change your value is returned here
    print('Player damage is', player2.Dmg)
    db.insertValue(player2,2)



    #changement de points de vie
def changePlayer2HP(HP):
    player2.maxHP=float(HP)
    #on input change your value is returned here
    print('Player health is', player2.maxHP)
    db.insertValue(player2,2)

    #changement de vitesse d'attaque
def changePlayer2atkspd(atkspd):
    player2.atkSpeed=atkspd
    #on input change your value is returned here
    print('Player attack speed is', player2.atkSpeed)
    db.insertValue(player2,2)


    #changement de nombre de vies
def changePlayer2Lives(lives):
    player2.lives=lives
    #on input change your value is returned here
    print('Player lives is', player2.lives)
    db.insertValue(player2,2)
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



