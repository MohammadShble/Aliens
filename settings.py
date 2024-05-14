class Settings():
    # a class to store all the setting for the game
    def __init__(self):
        # initialize
        self.screenWidth = 1200
        self.screenHeight = 800
        self.backgroundcolor = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
