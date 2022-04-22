import pygame.font

class ScoreBoard:
    def __init__(self, game):
        self.settings = game.settings
        self.window = game.window
        self.window_rect = self.window.get_rect()
        self.stats = game.stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.window_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.window.blit(self.score_image, self.score_rect)    
