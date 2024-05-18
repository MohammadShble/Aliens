class Settings():
    # a class to store all the setting for the game
    def __init__(self):
        # initialize the game's static settings -----------------
        self.screenWidth = 1200
        self.screenHeight = 800
        self.backgroundcolor = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3


        # Alien settings
        self.fleet_drop_speed = 20

        # a scale to speeding up the game 
        self.speed_up = 1.1

        # a scale to increase alien points
        self.score_scale = 1.5

        # initialize the game's dynamic settings ----------------
        self.initialize_dy_settings()

        # scoring
        self.alien_points = 50

    def initialize_dy_settings(self):
        # this is for the settings that change throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        # increase speed settings and alien points
        self.ship_speed *= self.speed_up
        self.bullet_speed *= self.speed_up
        self.alien_speed *= self.speed_up

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)