from random import randint
import pygame
import settings as stn

class PLAYER(pygame.sprite.Sprite):
    def __init__(self, x, y,img,name,score=0
    ,HP=500.0,
    Dmg=50,atkSpeed=15,lives=1):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.score=score
        self.maxHP=HP
        self.HP=self.maxHP
        self.lives=lives
        self.Dmg=Dmg
        self.atkSpeed=atkSpeed
        self.moveset = []
        self.image=pygame.Surface((60,60))
        self.image.fill(stn.RED)
        # self.image=pygame.image.load(os.path.join(stn.img_folder,img)).convert()
        self.image.set_colorkey(stn.BLACK)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.directionX=1
        self.directionY=0
        self.isDead=False
    def update(self):
        self.prevX=0

        #joueur va à gauche
        if self.moveset[0]:
            self.rect.x -= 5
            self.prevX=1
            self.directionX=1
            self.directionY=0
            if self.rect.right<0:
                self.rect.left=stn.WIDTH


        #joueur va à droite
        if self.moveset[1]:
            self.rect.x += 5
            self.prevX=1
            self.directionX=-1
            self.directionY=0
            if self.rect.left>stn.WIDTH:
                self.rect.right=0

        #joueur va en haut
        if self.moveset[2]:
            prevY=1
            self.rect.y -= 5
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
            self.rect.y += 5
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
        self.score+=score
    def decreaseScore(self,score):
        self.score-=score
        if self.score<0:
            self.score=0
    def increaseHp(self,HpAdded):
        self.HP+=HpAdded
        if self.HP>=self.maxHP:
            self.HP=self.maxHP

    def decreaseHP(self,dmg):
        self.HP-=dmg
        if self.HP<=0:
            self.isDead=True
            self.HP=0
    def respawn(self):
        if self.isDead:
            self.decreaseScore(100)
            x=randint(50,stn.WIDTH-50)
            y=randint(50,stn.HEIGHT-50)
            self.rect.center=(x,y)
            self.HP=self.maxHP
            self.lives-=1
            self.isDead=False

