from telnetlib import DO
import pygame
import sys
import os,json
# import screen

from model.collisions import bullet_Hit_Player
# from model.player import PLAYER
from model.bullet import BULLET
import model.menu as Menu
import model.displays as dsp
import settings as stn
import model.database as db
pygame.init()

display = pygame.display.set_mode((stn.WIDTH, stn.HEIGHT))
def set_difficulty(value, difficulty):
    # Do the job here !
    pass
clock = pygame.time.Clock()

joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()
with open(os.path.join("ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)
# 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
# 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }
def start_the_game():
    LEFT, RIGHT, UP, DOWN = False, False, False, False
    stn.player1,stn.player2=stn.InitSettings()
    all_sprites = pygame.sprite.Group() # tous les sprites
    bullets_P1=pygame.sprite.Group() # la sprite des bulletes du joueur 1 
    bullets_P2=pygame.sprite.Group() # la sprite des bulletes du joueur 2


    all_sprites.add(stn.player1) # ajout du joueur 1 dans le groupe des sprites
    all_sprites.add(stn.player2) # ajout du joueur 2 dans le groupe des sprites
    
    while True:
        stn.player1.setOpponent(stn.player2)
        stn.player2.setOpponent(stn.player1)
        # if stn.player2.isIA==True:
        stn.player2.makeIABulltets(bullets_P2)
        # print("player1 X = ",stn.player1.rect.x,"player1 Y = ",stn.player1.rect.y)
        textRect1,text1=dsp.displayScore(stn.player1)
        textRectHP1,textHP1=dsp.displayHp(stn.player1)
        textRectLives1,textLives1=dsp.displayLives(stn.player1)
        # set the center of the rectangular object.
        textRect1.topleft = (0,0)
        textRectHP1.topleft = (0,40)
        textRectLives1.topleft = (0,70)
        textRect2,text2=dsp.displayScore(stn.player2)
        textRectHP2,textHP2=dsp.displayHp(stn.player2)
        textRectLives2,textLives2=dsp.displayLives(stn.player2)
        textRect2.topright = (stn.WIDTH,0)
        textRectHP2.topright = (stn.WIDTH,40)
        textRectLives2.topright = (stn.WIDTH,70)
        player1MoveSet=[LEFT, RIGHT,
                       UP, DOWN]
        for event in pygame.event.get(): #pour la fermeture du jeu avec le bouton "X"
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT
            if event.type==pygame.KEYDOWN:
                # #P1 tir
                if event.key==pygame.K_m:
                    bullets_P1.add(BULLET(stn.player1.rect.x,stn.player1.rect.y,stn.player1.directionX,stn.player1.directionY,stn.player1.atkSpeed))
                #P2 tir
                if event.key==pygame.K_SPACE and stn.player2.isIA==False:
                    stn.player2.bullets.add(BULLET(stn.player2.rect.x,stn.player2.rect.y,stn.player2.directionX,stn.player2.directionY,stn.player2.atkSpeed))
                    # HANDLES BUTTON PRESSES
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == button_keys['x']:
                    bullets_P1.add(BULLET(stn.player1.rect.x,stn.player1.rect.y,stn.player1.directionX,stn.player1.directionY,stn.player1.atkSpeed))
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == button_keys['left_arrow']:
                    LEFT = True
                if event.button == button_keys['right_arrow']:
                    RIGHT = True
                if event.button == button_keys['down_arrow']:
                    DOWN = True
                if event.button == button_keys['up_arrow']:
                    UP = True
            # HANDLES BUTTON RELEASES
            if event.type == pygame.JOYBUTTONUP:
                if event.button == button_keys['left_arrow']:
                    LEFT = False
                if event.button == button_keys['right_arrow']:
                    RIGHT = False
                if event.button == button_keys['down_arrow']:
                    DOWN = False
                if event.button == button_keys['up_arrow']:
                    UP = False
            if event.type == pygame.JOYAXISMOTION:
                analog_keys[event.axis] = event.value
                # print(analog_keys)
                # Horizontal Analog
                if abs(analog_keys[0]) > .4:
                    if analog_keys[0] < -.7:
                        LEFT = True
                    else:
                        LEFT = False
                    if analog_keys[0] > .7:
                        RIGHT = True
                    else:
                        RIGHT = False
                # Vertical Analog
                if abs(analog_keys[1]) > .4:
                    if analog_keys[1] < -.7:
                        UP = True
                    else:
                        UP = False
                    if analog_keys[1] > .7:
                        DOWN = True
                    else:
                        DOWN = False
            # player1MoveSet=[LEFT, RIGHT,
            #            UP, DOWN]

        #Application des moveset
        #Récuperation des boutons
        keys = pygame.key.get_pressed()
        #listes des controlles des joueurs
        player1MoveSet=[keys[pygame.K_q] or LEFT, keys[pygame.K_d] or RIGHT,
                        keys[pygame.K_z] or UP, keys[pygame.K_s] or DOWN]
        stn.player1.changeMoveSet(player1MoveSet)
        player2MoveSet=[keys[pygame.K_h], keys[pygame.K_k],
                        keys[pygame.K_u], keys[pygame.K_j]]
        stn.player2.changeMoveSet(player2MoveSet)
        #mise à jour des mouvement
        bullets_P1.update()
        stn.player2.bullets.update()
        all_sprites.update()
        # #collision des bullets avec joueur1
        bullet_Hit_Player(stn.player2,stn.player1,stn.player2.bullets)
        #collision des bullets avec joueur2
        bullet_Hit_Player(stn.player1,stn.player2,bullets_P1)
        #60 FPS
        clock.tick(60)
        display.fill(stn.Gray) # le fond d'écran
        all_sprites.draw(display) #affichage des sprites 
        bullets_P1.draw(display) #affichage des sprites bullets du joueur 1
        stn.player2.bullets.draw(display) #affichage des sprites bullets du joueur 2
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display.blit(text1, textRect1)
        display.blit(textHP1, textRectHP1)
        display.blit(textLives1, textRectLives1)
        display.blit(text2, textRect2)
        display.blit(textHP2, textRectHP2)
        display.blit(textLives2, textRectLives2)
        if stn.player2.lives<=0 or stn.player1.lives<=0:
            print("dead")
            if stn.player1.score<stn.player2.score:
                string=stn.player2.name+" is the winner with "+str(stn.player2.score)+" score !!!"
                db.insertMatchData(stn.player2)
            else:
                string=stn.player1.name+" is the winner with "+str(stn.player1.score)+" score !!!"
                db.insertMatchData(stn.player1)
            stn.player1,stn.player2=stn.InitSettings()
            Menu.scoreEndGame(start_the_game,string)
            break
        pygame.display.update()
        
    pass
# start_the_game()
Menu.menuPrincipal(start_the_game,True)
# Menu.changePlayer1()


