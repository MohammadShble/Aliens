class GameStats():
    # tracks stats of the game
    def __init__(self, Game_settings):
        self.Game_settings = Game_settings
        self.reset_stats()

        # start the game with inactive state
        self.game_active = False

        # high score should never be reset
        self.high_score = 0
    
    def reset_stats(self):
        # initialize stats that can change during the game
        self.ships_left = self.Game_settings.ship_limit
        self.score = 0
        self.level = 1