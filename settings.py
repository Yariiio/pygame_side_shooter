class Settings():
    def __init__(self):
        # Window settings
        self.window_w = 1200
        self.window_h = 800
        self.bg_color = (175, 175, 175)

        # Player settings
        self.player_velocity = 1.5
        self.life_limit = 3

        #Bullet settings
        self.bullet_velocity = 2.0
        self.bullet_width = 15
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 20

        #Enemy settings
        self.enemy_velocity = 1.0