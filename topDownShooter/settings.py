import os
from model.player import PLAYER
#les couleurs
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
#la taille de l'écran
WIDTH=1500
HEIGHT=720
#le fichier des images
game_folder=os.path.dirname(__file__)
img_folder=game_folder
# img_folder=os.path.join(game_folder,"img")
player1 = PLAYER(WIDTH-50, HEIGHT-50,"Man 1.png","Midouch",atkSpeed=50) # joueur1
player2 = PLAYER(WIDTH-(player1.rect.x), HEIGHT-(player1.rect.y),"Man 1.png","CDM") # joueur2