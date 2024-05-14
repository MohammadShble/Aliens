import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, Game_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(Game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(Game_settings, screen, ship, bullets):
    # response to keypresses and mouse moves.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, Game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(Game_settings, screen, ship, bullets):
    # we create a new bullet and add it to the bullets group
    if len(bullets) < Game_settings.bullets_allowed:
        new_bullet = Bullet(Game_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    bullets.update()
    # get rid of old bullets (bullet that have disappeared)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    

def update_screen(Game_settings, screen, ship, bullets):
    # update the screen and the images on it.
    # draw the screen during each pass through the loop
    screen.fill(Game_settings.backgroundcolor)
    # redraw bullets behind the ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # make the screen(most recent one) visible        
    pygame.display.flip()
    