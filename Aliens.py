import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def rungame():
    # initialize the game and screen object
    pygame.init()
    Game_settings = Settings()
    # create the display window
    screen = pygame.display.set_mode((Game_settings.screenWidth,
                                        Game_settings.screenHeight))
    pygame.display.set_caption("Aliens")

    # create an instance to store the game's stats
    stats = GameStats(Game_settings)

     # make a ship instance, group of aliens and a group of bullets
    ship = Ship(Game_settings ,screen)
    aliens = Group()
    bullets = Group()

    # Background color
    bg_color = (230, 230, 230)

    # crate a fleet of aliens
    gf.create_fleet(Game_settings, screen, ship, aliens)

    # the main loop of the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(Game_settings, screen, ship, bullets) 

        if stats.game_active:
            ship.update()
            gf.update_bullets(Game_settings, screen, ship, aliens, bullets)
            gf.update_aliens(Game_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(Game_settings, screen, ship, aliens, bullets)


rungame()