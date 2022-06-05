import pygame
import sys
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
 

def start_the_game():
    stn.player1,stn.player2=stn.InitSettings()
    print(stn.player1.name)
    print(stn.player2.name)
    all_sprites = pygame.sprite.Group() # tous les sprites
    bullets_P1=pygame.sprite.Group() # la sprite des bulletes du joueur 1 
    bullets_P2=pygame.sprite.Group() # la sprite des bulletes du joueur 2


    all_sprites.add(stn.player1) # ajout du joueur 1 dans le groupe des sprites
    all_sprites.add(stn.player2) # ajout du joueur 2 dans le groupe des sprites
    
    while True:
        textRect1,text1=dsp.displayScore(stn.player1)
        textRectHP1,textHP1=dsp.displayHp(stn.player1)
        # set the center of the rectangular object.
        textRect1.topleft = (0,0)
        textRectHP1.topleft = (0,40)
        textRect2,text2=dsp.displayScore(stn.player2)
        textRectHP2,textHP2=dsp.displayHp(stn.player2)
        textRect2.topright = (stn.WIDTH,0)
        textRectHP2.topright = (stn.WIDTH,40)
        for event in pygame.event.get(): #pour la fermeture du jeu avec le bouton "X"
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT
            if event.type==pygame.KEYDOWN:
                #P1 tir
                if event.key==pygame.K_RETURN:
                    bullets_P1.add(BULLET(stn.player1.rect.x,stn.player1.rect.y,stn.player1.directionX,stn.player1.directionY,stn.player1.atkSpeed))
                #P2 tir
                if event.key==pygame.K_SPACE:
                    bullets_P2.add(BULLET(stn.player2.rect.x,stn.player2.rect.y,stn.player2.directionX,stn.player2.directionY,stn.player2.atkSpeed))
        #Récuperation des boutons
        keys = pygame.key.get_pressed()
        #listes des controlles des joueurs
        player1MoveSet=[keys[pygame.K_q], keys[pygame.K_d],
                        keys[pygame.K_z], keys[pygame.K_s]]
        player2MoveSet=[keys[pygame.K_h], keys[pygame.K_k],
                        keys[pygame.K_u], keys[pygame.K_j]]
        #Application des moveset
        stn.player1.changeMoveSet(player1MoveSet)
        stn.player2.changeMoveSet(player2MoveSet)
        #mise à jour des mouvement
        bullets_P1.update()
        bullets_P2.update()
        all_sprites.update()
        # #collision des bullets avec joueur1
        bullet_Hit_Player(stn.player2,stn.player1,bullets_P2)
        #collision des bullets avec joueur2
        bullet_Hit_Player(stn.player1,stn.player2,bullets_P1)
        #60 FPS
        clock.tick(60)
        display.fill(stn.BLACK) # le fond d'écran
        all_sprites.draw(display) #affichage des sprites 
        bullets_P1.draw(display) #affichage des sprites bullets du joueur 1
        bullets_P2.draw(display) #affichage des sprites bullets du joueur 2
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display.blit(text1, textRect1)
        display.blit(textHP1, textRectHP1)
        display.blit(text2, textRect2)
        display.blit(textHP2, textRectHP2)
        if stn.player2.lives<=0 or stn.player1.lives<=0:
            print("dead")
            if stn.player1.score<stn.player2.score:
                string=stn.player2.name+" is the winner with "+str(stn.player2.score)+" score !!!"
            else:
                string=stn.player1.name+" is the winner with "+str(stn.player1.score)+" score !!!"
            db.insertMatchData(stn.player1,stn.player2)
            stn.player1,stn.player2=stn.InitSettings()
            Menu.scoreEndGame(start_the_game,string)
            break
        pygame.display.update()
        
    pass
# start_the_game()
Menu.menuPrincipal(start_the_game,True)
# Menu.changePlayer1()


