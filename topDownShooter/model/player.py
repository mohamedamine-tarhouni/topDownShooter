import pygame
from model.bullet import BULLET
import settings as stn
import os

class PLAYER(pygame.sprite.Sprite):
    def __init__(self, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        self.moveset = []
        self.image=pygame.image.load(os.path.join(stn.img_folder,img)).convert()
        self.image.set_colorkey(stn.BLUE)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.directionX=1
        self.directionY=0
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
