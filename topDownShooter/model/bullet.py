import pygame
import math
# from turtle import width
class BULLET:
    def __init__(self,x,y,directionB):
        self.x=x
        self.y=y
        self.speed=10
        self.directionB=directionB
    def main(self,display):
        if(self.directionB=="right"):
            self.x+=1*self.speed
        if(self.directionB=="left"):
            self.x-=1*self.speed
        if(self.directionB=="up"):
            self.y-=1*self.speed
        if(self.directionB=="down"):
            self.y+=1*self.speed
        
        pygame.draw.circle(display,(0,0,0),(self.x,self.y),5)
