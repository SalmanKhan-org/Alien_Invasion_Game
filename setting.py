class Settings:
    """A class to store all settings for the Alien Invasion"""
    def __init__(self):
        """Initialize the game's setting"""
        #Screen setting
        self.ship_speed = 1.5
        self.ships_limit = 3
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Bullet setting
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 4

        #Alien Setting
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet direction 1 represent right and -1 represent left
        self.fleet_direction = 1

        #How quickly the game speed up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that will change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        