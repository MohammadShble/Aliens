import pygame

class Ship():
    def __init__(self, screen):
        # initialize the ship and its starting position.
        self.screen = screen

        # load the ship image and
        self.image = pygame.image.load('images/ship.bmp')

        # get the image's rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    # A function to draw the ship
    def blitme(self):
        # Draw the ship at its current position
        self.screen.blit(self.image, self.rect)