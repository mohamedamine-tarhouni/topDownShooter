import pygame
import sys
import sqlite3
from model.player import PLAYER
from model.bullet import BULLET
import model.menu as Menu
import model.settings as stn
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

def start_the_game():
    all_sprites = pygame.sprite.Group()
    player1 = PLAYER(400, 300) #joueur1
    player2 = PLAYER(100, 100) #joueur2
    all_sprites.add(player1)#ajout du joueur 1 dans le groupe des sprites
    all_sprites.add(player2)#ajout du joueur 2 dans le groupe des sprites
    player1_Bullets=[] #liste des bullets du P1
    player2_Bullets=[] #liste des bullets du P2
    
    while True:
        display.fill((24, 164, 86)) # le fond d'écran
        all_sprites.draw(display) #affichage de fond 
        for event in pygame.event.get(): #pour la fermeture du jeu avec le bouton "X"
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT
            if event.type==pygame.KEYDOWN:
                #P1 tir
                if event.key==pygame.K_RETURN:
                    player1_Bullets.append(BULLET(player1.rect.x,player1.rect.y,player1.directionX,player1.directionY))
                #P2 tir
                if event.key==pygame.K_SPACE:
                    player2_Bullets.append(BULLET(player2.rect.x,player2.rect.y,player2.directionX,player2.directionY))
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
        all_sprites.update()
        #traitement de chaque bullet
        for bullet in player1_Bullets:
            bullet.main(display)
        for bullet in player2_Bullets:
            bullet.main(display)
        #60 FPS
        clock.tick(60)
        pygame.display.update()
    pass

Menu.menuPrincipal(start_the_game)

