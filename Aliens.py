import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def rungame():
    # initialize the game and screen object
    pygame.init()
    Game_settings = Settings()
    # create the display window
    screen = pygame.display.set_mode((Game_settings.screenWidth,
                                        Game_settings.screenHeight))
    pygame.display.set_caption("Aliens")

     # make a ship instance.
    ship = Ship(Game_settings ,screen)

    # make a group to store the bullets
    bullets = Group()

    # Background color
    bg_color = (230, 230, 230)

        # the main loop of the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(Game_settings, screen, ship, bullets) 
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(Game_settings, screen, ship, bullets)


rungame()