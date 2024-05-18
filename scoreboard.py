import pygame.font

class Scoreboard():
    # a class to report scoring info
    def __init__(self, Game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.Game_settings = Game_settings
        self.stats = stats

        # font settings for scoring
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        # turns the score into a rendered image
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.Game_settings.backgroundcolor)
        
        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
