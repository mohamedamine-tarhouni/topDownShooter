import pygame_menu
from pygame_menu.examples import create_example_window

def menuPrincipal(funcStart):

    menu = pygame_menu.Menu('Welcome', 800, 600,
                        theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name :', default='John Doe')
    # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add.button('Play', funcStart)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    surface = create_example_window('Example - Simple', (800, 600))
    menu.mainloop(surface)