from hashlib import new
import pygame
import pygame_menu
import sys
from model.player import PLAYER
from model.bullet import BULLET
from pygame_menu.examples import create_example_window
pygame.init()
player1 = PLAYER(400, 300, 32, 32)
player2 = PLAYER(100, 100, 32, 32)


display_Scroll = [0, 0]
player1_Bullets=[]
player2_Bullets=[]
display = pygame.display.set_mode((800, 600))
def set_difficulty(value, difficulty):
    # Do the job here !
    pass
clock = pygame.time.Clock()
def start_the_game():
    while True:
        display.fill((24, 164, 86))
        # mouse_x,mouse_y=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    player1_Bullets.append(BULLET(player1.x,player1.y,player1.direction))
                if event.key==pygame.K_SPACE:
                    player2_Bullets.append(BULLET(player2.x,player2.y,player2.direction))
        keys = pygame.key.get_pressed()
        player1MoveSet=[keys[pygame.K_q], keys[pygame.K_d],
                        keys[pygame.K_z], keys[pygame.K_s],keys[pygame.KEYDOWN]]
        player2MoveSet=[keys[pygame.K_LEFT], keys[pygame.K_RIGHT],
                        keys[pygame.K_UP], keys[pygame.K_DOWN],keys[pygame.K_KP_ENTER]]
        player1.changeMoveSet(player1MoveSet)
        player2.changeMoveSet(player2MoveSet)
        # pygame.draw.rect(display,(255,255,255),(100-display_Scroll[0],100-display_Scroll[1],16,16))
        player1.move()
        player2.move()
        player1.main(display)
        player2.main(display)
        for bullet in player1_Bullets:
            bullet.main(display)
        for bullet in player2_Bullets:
            bullet.main(display)
        clock.tick(60)
        pygame.display.update()
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
surface = create_example_window('Example - Simple', (800, 600))
menu.mainloop(surface)


