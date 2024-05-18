import pygame.font

class Button():
    def __init__(self, Game_settings, screen, msg):
        # initialize button
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # dimensions and properties of the button.
        self.width = 200
        self.height = 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # the button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # the button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turns msg into a rendered image
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw_button(self):
        # draw blank button and then draw the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)