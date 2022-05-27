import pygame
import settings as stn
class BULLET(pygame.sprite.Sprite):
    def __init__(self,x,y,directionBX,directionBY):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((40,40))
        self.image.fill(stn.BLUE)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.speed=10
        self.directionBX=directionBX
        self.directionBY=directionBY
    def update(self):
        self.rect.x-=self.directionBX*self.speed
        self.rect.y-=self.directionBY*self.speed
