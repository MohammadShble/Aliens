import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # this class represents a single alien
    def __init__(self, Game_settings, screen):
        # initializing the alien and set it's starting position
        super().__init__()
        self.screen = screen
        self.Game_settings = Game_settings

        # load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        # set the alien's rect
        self.rect = self.image.get_rect()

        # initial position
        self.rect.x = self.rect.width - 80
        self.rect.y = self.rect.height - 100

        #store the alien's exact position
        self.x = float(self.rect.x)
    
    def blitme(self):
        # draw the alien at it's current position
        self.screen.blit(self.image, self.rect)