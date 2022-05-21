import pygame
from model.bullet import BULLET

class PLAYER:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moveset = []
        self.direction="left"

    def main(self, display):
        pygame.draw.rect(display, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))

    def move(self):
        if self.moveset[0]:
            self.x -= 5
            self.direction="left"
        if self.moveset[1]:
            self.x += 5
            self.direction="right"
        if self.moveset[2]:
            self.y -= 5
            self.direction="up"
        if self.moveset[3]:
            self.y += 5
            self.direction="down"

    def changeMoveSet(self, buttons):
        self.moveset = [buttons[0],buttons[1],buttons[2],buttons[3],buttons[4]]
