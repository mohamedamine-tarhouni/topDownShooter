import pygame
import sys
# import screen
import sqlite3
from model.player import PLAYER
from model.bullet import BULLET
import model.menu as Menu
import settings as stn
pygame.init()
# connection = sqlite3.connect('score.db')

# cursor = connection.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS ScoreBoard
#   (
#         Player1Name    TEXT,
#         Player2Name    TEXT,
#         Player1Score    INT,
#         Player2Score    INT
#   ); 
#     '''
#     )
# # send to database one query
# Game = ('midouch', 'amine',2365,259)
# # cursor.execute('INSERT INTO score VALUES (?,?)', Best_User)
# cursor.execute('INSERT INTO ScoreBoard VALUES (?,?,?,?)', Game)

# connection.commit()
# # print the first
# cursor.execute("SELECT * FROM ScoreBoard")
# # record = cursor.fetchone()
# # print all
# record = cursor.fetchall()
# # print a specific number of entry
# # record = cursor.fetchmany(2)

# # loop to print line by line
# # for records in record:
#     # print(record)

# print(record)

# connection.close()

display = pygame.display.set_mode((stn.WIDTH, stn.HEIGHT))
def set_difficulty(value, difficulty):
    # Do the job here !
    pass
clock = pygame.time.Clock()
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 

def start_the_game():

    all_sprites = pygame.sprite.Group() # tous les sprites
    bullets_P1=pygame.sprite.Group() #la sprite des bulletes du joueur 1 
    bullets_P2=pygame.sprite.Group() #la sprite des bulletes du joueur 2
    player1 = PLAYER(400, 300,"Man 1.png","Midouch",atkSpeed=50) #joueur1
    player2 = PLAYER(100, 100,"Man 1.png","CDM") #joueur2

    all_sprites.add(player1)#ajout du joueur 1 dans le groupe des sprites
    all_sprites.add(player2)#ajout du joueur 2 dans le groupe des sprites
    
    while True:
        # create a text surface object,
        # on which text is drawn on it.
        text1 = font.render(player1.name+" : "+str(player1.score), True, stn.GREEN, stn.BLUE)
        
        # create a rectangular object for the
        # text surface object
        textRect1 = text1.get_rect()
        
        # set the center of the rectangular object.
        textRect1.topleft = (0,0)
        text2 = font.render(player2.name+" : "+str(player2.score), True, stn.GREEN, stn.BLUE)
        textRect2 = text2.get_rect()
        textRect2.topright = (stn.WIDTH,0)
        for event in pygame.event.get(): #pour la fermeture du jeu avec le bouton "X"
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT
            if event.type==pygame.KEYDOWN:
                #P1 tir
                if event.key==pygame.K_RETURN:
                    bullets_P1.add(BULLET(player1.rect.x,player1.rect.y,player1.directionX,player1.directionY,50))
                #P2 tir
                if event.key==pygame.K_SPACE:
                    bullets_P2.add(BULLET(player2.rect.x,player2.rect.y,player2.directionX,player2.directionY,100))
        #Récuperation des boutons
        keys = pygame.key.get_pressed()
        #listes des controlles des joueurs
        player1MoveSet=[keys[pygame.K_q], keys[pygame.K_d],
                        keys[pygame.K_z], keys[pygame.K_s]]
        player2MoveSet=[keys[pygame.K_h], keys[pygame.K_k],
                        keys[pygame.K_u], keys[pygame.K_j]]
        #Application des moveset
        player1.changeMoveSet(player1MoveSet)
        player2.changeMoveSet(player2MoveSet)
        #mise à jour des mouvement
        bullets_P1.update()
        bullets_P2.update()
        all_sprites.update()
        #collision des bullets avec joueur2
        hit_On_P1=pygame.sprite.spritecollide(player1,bullets_P2,True)
        if hit_On_P1:
            player2.updateScore(50)
            print("player 2 :",player2.score)
            print("joueur 1 touché par un bullet")
        #collision des bullets avec joueur2
        hit_On_P2=pygame.sprite.spritecollide(player2,bullets_P1,True)
        if hit_On_P2:
            player1.updateScore(50)
            print("player 1 :",player1.score)
            print("joueur 2 touché par un bullet")
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
        display.blit(text2, textRect2)
        pygame.display.update()
    pass

Menu.menuPrincipal(start_the_game)

