import pygame


class PLAYER:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moveset = []

    def main(self, display):
        pygame.draw.rect(display, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))

    def move(self):
        if self.moveset[0]:
            self.x -= 5
        if self.moveset[1]:
            self.x += 5
        if self.moveset[2]:
            self.y -= 5
        if self.moveset[3]:
            self.y += 5

    def changeMoveSet(self, buttons):
        self.moveset = [buttons[0],buttons[1],buttons[2],buttons[3]]
