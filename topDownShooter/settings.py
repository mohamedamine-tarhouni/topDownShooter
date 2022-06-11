import os
from model.player import PLAYER
import model.database as db
#les couleurs
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
MediumOrchid=(186, 85, 211)
#la taille de l'écran
WIDTH=800
HEIGHT=600
#le fichier des images
game_folder=os.path.dirname(__file__)
img_folder=game_folder
# img_folder=os.path.join(game_folder,"img")
    
def InitSettings():
    player1Data=db.getPlayerData(1)
    print(player1Data)
    player2Data=db.getPlayerData(2)
    if player1Data:
        player1 = PLAYER(WIDTH-100, HEIGHT-100,"Man 1.png",player1Data[0][0],1,score=0
        ,HP=player1Data[0][2],Dmg=player1Data[0][3],atkSpeed=player1Data[0][4],lives=player1Data[0][1],speed=player1Data[0][5],color=GREEN)
    else:
        player1 = PLAYER(WIDTH-100, HEIGHT-100,"Man 1.png","Midouch",1,atkSpeed=50,color=GREEN) # joueur1
    if player2Data:
        player2 = PLAYER(WIDTH-(player1.rect.x), HEIGHT-(player1.rect.y),"Man 1.png",player2Data[0][0],2,score=0
        ,HP=player2Data[0][2],Dmg=player2Data[0][3],atkSpeed=player2Data[0][4],lives=player2Data[0][1],speed=player2Data[0][5],isIA=True,color=MediumOrchid)
    else:
        player2 = PLAYER(WIDTH-(player1.rect.x), HEIGHT-(player1.rect.y),"Man 1.png","CDM",2,True,color=MediumOrchid) # joueur2
    return player1,player2
player1,player2=InitSettings()