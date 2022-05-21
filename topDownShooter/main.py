from hashlib import new
import pygame
import sys
from model.player import PLAYER
pygame.init()
player1 = PLAYER(400, 300, 32, 32)
player2 = PLAYER(100, 100, 32, 32)


display_Scroll = [0, 0]
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
while True:
    display.fill((24, 164, 86))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
    keys = pygame.key.get_pressed()
    player1MoveSet=[keys[pygame.K_q], keys[pygame.K_d],
                    keys[pygame.K_z], keys[pygame.K_s]]
    player2MoveSet=[keys[pygame.K_LEFT], keys[pygame.K_RIGHT],
                    keys[pygame.K_UP], keys[pygame.K_DOWN]]
    player1.changeMoveSet(player1MoveSet)
    player2.changeMoveSet(player2MoveSet)
    # pygame.draw.rect(display,(255,255,255),(100-display_Scroll[0],100-display_Scroll[1],16,16))
    player1.move()
    player2.move()
    player1.main(display)
    player2.main(display)

    clock.tick(60)
    pygame.display.update()
