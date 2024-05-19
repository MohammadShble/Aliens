import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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


def check_events(Game_settings, screen, stats, ScoreBoard,
                  play_button, ship, aliens, 
                  bullets):
    # response to keypresses and mouse moves.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, Game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(Game_settings, screen, stats, ScoreBoard,
                                play_button, ship, aliens, 
                                bullets, mouse_x, mouse_y)


def check_play_button(Game_settings, screen, stats, ScoreBoard,
                      play_button, ship, aliens, 
                      bullets, mouse_x, mouse_y):
    # start a new game when the player presses play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) 
    # to deactivate the play button
    # when the game is running
    if button_clicked and not stats.game_active:
            
            # reset the game settings
            Game_settings.initialize_dy_settings()

            # hide the mouse cursor
            pygame.mouse.set_visible(False)

            # reset the game stats
            stats.reset_stats()
            stats.game_active = True
            
            # reset scoreboard images
            ScoreBoard.prep_score()
            ScoreBoard.prep_high_score()
            ScoreBoard.prep_level()
            ScoreBoard.prep_ships()

            aliens.empty()
            bullets.empty()

            create_fleet(Game_settings, screen, ship, aliens)
            ship.center_ship()


def fire_bullet(Game_settings, screen, ship, bullets):
    # we create a new bullet and add it to the bullets group
    if len(bullets) < Game_settings.bullets_allowed:
        new_bullet = Bullet(Game_settings, screen, ship)
        bullets.add(new_bullet)



def check_bullet_alien_collisions(Game_settings, screen, stats,
                                  ScoreBoard, ship, aliens, bullets):
    # respond to any bullet-alien collision 
    # remove the bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        # this 'for' loop is for making sure that the player gets points
        # for all the hits
        # for example if two hits happend during the same pass through the loop
        # or the bullet is wide enough to hit more than one alien at the same time
        # the player will get points only for one hit
        for aliens in collisions.values():
            stats.score += Game_settings.alien_points * len(aliens)
            ScoreBoard.prep_score()
        check_high_score(stats, ScoreBoard)

    if len(aliens) == 0:
        # destroy the existing bullets and create a new fleet of aliens
        # speed up the game
        bullets.empty()
        Game_settings.increase_speed()

        # increase level
        stats.level += 1
        ScoreBoard.prep_level()

        create_fleet(Game_settings, screen, ship, aliens)



def update_bullets(Game_settings, screen, stats,
                    ScoreBoard, ship, aliens, bullets):
    bullets.update()
    # get rid of old bullets (bullet that have disappeared)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(Game_settings, screen, stats,
                                  ScoreBoard, ship, aliens, bullets)


    



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

    # create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(num_of_aliens_x):
            create_alien(Game_settings, screen, aliens, alien_number, row_number)





def check_fleet_edges(Game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(Game_settings, aliens)
            break


def check_aliens_bottom(Game_settings, screen, stats, ScoreBoard, ship, aliens, bullets):
    # check if any alien has reached the bottom of the screen
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # same situation as the ship got hit
            ship_hit(Game_settings, screen, stats, ScoreBoard, ship, aliens, bullets)
            break


def check_high_score(stats, ScoreBoard):
    # this checks if there is a new high score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        ScoreBoard.prep_high_score()


def change_fleet_direction(Game_settings, aliens):
    # drop the entire fleet down and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += Game_settings.fleet_drop_speed
    Game_settings.fleet_direction *= -1


def update_aliens(Game_settings, screen, stats, ScoreBoard, ship, aliens, bullets):
    # check if the fleet is at an edge 
    # the update the position of all the aliens
    check_fleet_edges(Game_settings, aliens)
    aliens.update()

    # to detect alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(Game_settings, screen, stats, ScoreBoard, ship, aliens, bullets)

    # check if an alien has hit the bottom of the screen
    check_aliens_bottom(Game_settings, screen, stats, ScoreBoard, ship, aliens, bullets)



def ship_hit(Game_settings, screen, stats, ScoreBoard, ship, aliens, bullets):
    # responds to ship-alien collisions
    
    if stats.ships_left > 0:
        # decrease ships_left
        stats.ships_left -= 1

        # update scoreboard
        ScoreBoard.prep_ships()

        # delete all the aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet of aliens 
        # position the ship at the center of the screen
        create_fleet(Game_settings, screen, ship, aliens)
        ship.center_ship()

        # pause the game a bit
        sleep(0.5)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_screen(Game_settings, screen, stats, 
                        ScoreBoard, ship, aliens, 
                        bullets, play_button):
    # update the screen and the images on it.
    # draw the screen during each pass through the loop
    screen.fill(Game_settings.backgroundcolor)
    # redraw bullets behind the ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    # draw the score info
    ScoreBoard.show_score()

    # darw the play button if the game is inactivated
    if not stats.game_active:
        play_button.draw_button()

    # make the screen(most recent one) visible        
    pygame.display.flip()
    