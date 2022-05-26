import pygame
class BULLET:
    def __init__(self,x,y,directionBX,directionBY):
        self.x=x
        self.y=y
        self.speed=10
        self.directionBX=directionBX
        self.directionBY=directionBY
    def main(self,display):
        self.x-=self.directionBX*self.speed
        self.y-=self.directionBY*self.speed
        
        pygame.draw.circle(display,(0,0,0),(self.x,self.y),5)
