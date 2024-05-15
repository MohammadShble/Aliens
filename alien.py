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


    def check_edges(self):
        # returns True if the alien is at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        

    def update(self):
        # moves the alien right or left
        self.x += (self.Game_settings.alien_speed * 
                        self.Game_settings.fleet_direction)
        self.rect.x = self.x




    
    def blitme(self):
        # draw the alien at it's current position
        self.screen.blit(self.image, self.rect)