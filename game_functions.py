import sys
import pygame

def check_events():
    # response to keypresses and mouse moves.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(Game_settings, screen, ship):
    # update the screen and the images on it.
    # draw the screen during each pass through the loop
    screen.fill(Game_settings.backgroundcolor)
    ship.blitme()

    # make the screen(most recent one) visible        
    pygame.display.flip()
    