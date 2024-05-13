import pygame

class Ship():
    def __init__(self, Game_settings, screen):
        # initialize the ship and its starting position.
        self.screen = screen
        self.Game_settings = Game_settings

        # load the ship image and
        self.image = pygame.image.load('images/ship.bmp')

        # get the image's rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store the ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update_ship(self):
        # moving the ship based on the flags value
        # we update the ship's center value not the rect
        # the second condition of the 'if' limits the ship's renge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.Game_settings.ship_speed
            
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.Game_settings.ship_speed

        # now we update the rect's centerx
        self.rect.centerx = self.center


    # A function to draw the ship
    def blitme(self):
        # Draw the ship at its current position
        self.screen.blit(self.image, self.rect)