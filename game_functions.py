import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, Game_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(Game_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


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
    



def get_number_of_aliens_x(Game_settings, alien_width):
    available_space_x = Game_settings.screenWidth - 2 * alien_width
    num_of_aliens_x = int(available_space_x / (2 * alien_width))
    return num_of_aliens_x



def get_number_of_aliens_y(Game_settings, ship_height, alien_height):
    # to determine the number of rows of aliens fit on the screen
    available_space_y = (Game_settings.screenHeight - (6 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows





def create_alien(Game_settings, screen, aliens, alien_number, row_number):
    # create an alien and place in it's position on the row
    alien = Alien(Game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)




def create_fleet(Game_settings, screen, ship, aliens):
    # create a full fleet of aliens
    # the space between two aliens is equal to the width of one alien
    alien = Alien(Game_settings, screen)

    alien_width = alien.rect.width
    alien_height = alien.rect.height

    ship_height = ship.rect.height

    num_of_aliens_x = get_number_of_aliens_x(Game_settings, alien_width)
    number_rows = get_number_of_aliens_y(Game_settings, ship_height, alien_height)
    print(number_rows)

    # create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(num_of_aliens_x):
            create_alien(Game_settings, screen, aliens, alien_number, row_number)





def check_fleet_edges(Game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(Game_settings, aliens)
            break



def change_fleet_direction(Game_settings, aliens):
    # drop the entire fleet down and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += Game_settings.fleet_drop_speed
    Game_settings.fleet_direction *= -1


def update_aliens(Game_settings, aliens):
    # check if the fleet is at an edge 
    # the update the position of all the aliens
    check_fleet_edges(Game_settings, aliens)
    aliens.update()





def update_screen(Game_settings, screen, ship, aliens, bullets):
    # update the screen and the images on it.
    # draw the screen during each pass through the loop
    screen.fill(Game_settings.backgroundcolor)
    # redraw bullets behind the ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # make the screen(most recent one) visible        
    pygame.display.flip()
    