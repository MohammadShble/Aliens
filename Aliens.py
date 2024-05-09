import sys
import pygame
from settings import Settings
from ship import Ship

def rungame():
    # initialize the game and screen object
    pygame.init()
    Game_Settings = Settings()
    # create the display window
    screen = pygame.display.set_mode((Game_Settings.screenWidth,
                                        Game_Settings.screenHeight))
    pygame.display.set_caption("Aliens")

     # make a ship instance.
    ship = Ship(screen)

    # Background color
    bg_color = (230, 230, 230)

        # the main loop of the game
    while True:
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(Game_Settings.backgroundcolor)
        ship.blitme()

        # make the screen(most recent one) visible        
        pygame.display.flip()


rungame()