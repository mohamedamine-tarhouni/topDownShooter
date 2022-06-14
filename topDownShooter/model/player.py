from audioop import mul
from random import randint
import pygame
import model.bullet as blt
import settings as stn
import model.database as db

class PLAYER(pygame.sprite.Sprite):
    def __init__(self, x, y,img,name,pos,score=0
    ,HP=500.0,
    Dmg=50,atkSpeed=15,lives=1,speed=15,isIA=False,color=(255,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.score=score
        self.maxHP=HP
        self.HP=self.maxHP
        self.lives=lives
        self.Dmg=Dmg
        self.atkSpeed=atkSpeed
        self.speed=speed
        self.isIA=isIA
        self.pos=pos
        self.moveset = []
        self.image=pygame.Surface((60,60))
        self.image.fill(color)
        # self.image=pygame.image.load(os.path.join(stn.img_folder,img)).convert()
        self.image.set_colorkey(stn.BLACK)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.directionX=1
        self.directionY=0
        self.isDead=False

        
    def update(self):
        if self.isIA:
            # print("je suis un IA")
            self.IAbhvr()
        else:
            self.prevX=0

            #joueur va à gauche
            if self.moveset[0]:
                self.rect.x -= self.speed
                self.prevX=1
                self.directionX=1
                self.directionY=0
                if self.rect.right<0:
                    self.rect.left=stn.WIDTH


            #joueur va à droite
            if self.moveset[1]:
                self.rect.x += self.speed
                self.prevX=1
                self.directionX=-1
                self.directionY=0
                if self.rect.left>stn.WIDTH:
                    self.rect.right=0

            #joueur va en haut
            if self.moveset[2]:
                prevY=1
                self.rect.y -= self.speed
                if self.prevX<=0:
                    self.directionX=0
                else:
                    prevY=0
                self.directionY=prevY
                if self.rect.bottom<0:
                    self.rect.top=stn.HEIGHT

            #joueur va en bas
            if self.moveset[3]:
                prevY=-1
                self.rect.y += self.speed
                if self.prevX<=0:
                    self.directionX=0
                else:
                    prevY=0
                self.directionY=prevY
                if self.rect.top>stn.HEIGHT:
                    self.rect.bottom=0

    def changeMoveSet(self, buttons):
        self.moveset = [buttons[0],buttons[1],buttons[2],buttons[3]]
    def updateScore(self,score):
        # multiplier=200000
        multiplier=50000//(((self.maxHP+self.atkSpeed+self.Dmg+self.lives)))
        
        # multiplier=multiplier//self.maxHP
        # multiplier=multiplier//self.Dmg
        # multiplier=multiplier//self.atkSpeed
        # score=score//self.lives
        self.score+=multiplier*score+2500
    def decreaseScore(self,score):
        self.score-=score
        if self.score<0:
            self.score=0
    def increaseHp(self,HpAdded):
        self.HP+=HpAdded
        if self.HP>=self.maxHP:
            self.HP=self.maxHP
    def decreaseLives(self):
        self.lives-=1
        if(self.lives<=0):
            self.decreaseScore(self.score//2)
    def decreaseHP(self,dmg):
        self.HP-=dmg
        if self.HP<=0:
            self.isDead=True
            self.HP=0
    def respawn(self,player):
        if self.isDead:
            self.decreaseScore(100)
            x=randint(50,stn.WIDTH-50)
            y=randint(50,stn.HEIGHT-50)
            self.rect.center=(x,y)
            self.HP=self.maxHP
            self.decreaseLives()
            player.updateScore(500)
            self.isDead=False
    def changeName(self,name):
        if(name!=""):
            self.name=name
            db.insertValue(self,self.pos)
        print(self.name)
        #changement de dégat
    def changePlayerDamage(self,dmg):
        if(dmg!="" and dmg.isnumeric()):
            self.Dmg=int(dmg)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player damage is', self.Dmg)


        #changement de points de vie
    def changePlayerHP(self,HP):
        if(HP!="" and HP.isnumeric()):
            self.maxHP=float(HP)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player health is', self.maxHP)

        #changement de vitesse d'attaque
    def changePlayeratkspd(self,atkspd):
        if(atkspd!="" and atkspd.isnumeric()):
            self.atkSpeed=int(atkspd)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player attack speed is', self.atkSpeed)


        #changement de nombre de vies
    def changePlayerLives(self,lives):
        if(lives!="" and lives.isnumeric()):
            self.lives=int(lives)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player lives is', self.lives)


        #changement de vitesse de déplacement
    def changePlayerSpeed(self,speed):
        if(speed!="" and speed.isnumeric()):
            self.speed=int(speed)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player speed is', self.speed)
    
    def setIA(self):
        self.isIA=not(self.isIA)
        print(self.isIA)
        db.insertValue(self,self.pos)

    def setOpponent(self,opponent):
        self.opponent=opponent
    def makeIABulltets(self,bullets):
        self.bullets=bullets
        self.previous_time = pygame.time.get_ticks()
    def IAbhvr(self):
        advSpeed=self.speed
        distX=self.rect.x-self.opponent.rect.x
        distY=self.rect.y-self.opponent.rect.y
        distanceX=abs(distX)
        distanceY=abs(distY)
        # print("distance x : ",distX)
        # print("distance y : ",distY)
        # print("distance absolute x : ",distanceX)
        # print("distance absolute y : ",distanceY)
        if distanceX<distanceY:
            if distX<0 and distanceX>advSpeed:
                self.rect.x += advSpeed
                if self.rect.left>stn.WIDTH-50:
                    self.rect.right=0
            elif distX>0 and distanceX>advSpeed:
                self.rect.x -= advSpeed
                if self.rect.right<50:
                    self.rect.left=stn.WIDTH
            elif distanceX<=15:
                print("on est en attaque X")
                if distY<0:
                    current_time = pygame.time.get_ticks()
                    current_time+=5
                    self.directionX=0
                    self.directionY=-1
                    if current_time % 15==0:
                        self.bullets.add(blt.BULLET(self.rect.x,self.rect.y,self.directionX,self.directionY,self.atkSpeed))
                        self.previous_time=current_time
                    
                else:
                    current_time = pygame.time.get_ticks()
                    current_time+=5
                    self.directionX=0
                    self.directionY=1
                    if current_time % 15==0:
                        self.bullets.add(blt.BULLET(self.rect.x,self.rect.y,self.directionX,self.directionY,self.atkSpeed))
                        self.previous_time=current_time  
                advSpeed=self.speed 
            elif distanceX<advSpeed:
                advSpeed-=1  
            
        else:
            if distY<0 and distanceY>advSpeed:
                self.rect.y += advSpeed
                if self.rect.top>stn.HEIGHT-50:
                    self.rect.bottom=0
            elif distY>0 and distanceY>advSpeed:
                self.rect.y -= advSpeed
                if self.rect.bottom<50:
                    self.rect.top=stn.HEIGHT
            elif distanceY<=15:
                # print("on est en attaque Y")
                if distX<0:
                    current_time = pygame.time.get_ticks()
                    current_time+=5
                    self.directionX=-1
                    self.directionY=0
                    # print("previous time  ",self.previous_time)
                    # print("current time : ",current_time)
                    if current_time % 15==0:
                        self.bullets.add(blt.BULLET(self.rect.x,self.rect.y,self.directionX,self.directionY,self.atkSpeed))
                        self.previous_time=current_time
                else:
                    current_time = pygame.time.get_ticks()
                    current_time+=5
                    self.directionX=1
                    self.directionY=0
                    # print("previous time  ",self.previous_time)
                    # print("current time : ",current_time)
                    if current_time % 15==0:
                        self.bullets.add(blt.BULLET(self.rect.x,self.rect.y,self.directionX,self.directionY,self.atkSpeed))
                        self.previous_time=current_time      
                advSpeed=self.speed
            elif distanceY<advSpeed:
                advSpeed-=1              

                    



