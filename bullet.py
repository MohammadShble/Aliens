import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, Game_settings, screen, ship):
        # creates a bullet at the ship's current position
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, Game_settings.bullet_width,
                                Game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the position of the bullet as float
        self.y = float(self.rect.y)

        self.color = Game_settings.bullet_color
        self.bullet_speed = Game_settings.bullet_speed

    def update(self):
        # moving the bullet up the screen
        self.y -= self.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)